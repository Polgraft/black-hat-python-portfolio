import socket
import sys
import argparse

def create_client(target_host, target_port):
    """Creates a TCP socket object and establishes a connection."""
    try:
        # AF_INET - IPv4, SOCK_STREAM = TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[*] Connecting to {target_host}:{target_port}...")
        client.connect((target_host, target_port))
        print("[+] Connection successful.")
        return client
    except socket.error as e:
        print(f"[-] Failed to connect: {e}")
        # Exit gracefully on connection failure
        sys.exit(1)
def send_and_receive(client, host):
    """Sends an HTTP GET request and receives the response."""
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    try:
        print(f"[*] Sending request to {host}...")
        client.sendall(request.encode('utf-8'))
        
        response_data = b""
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response_data += chunk
        
        return response_data.decode('utf-8', 'ignore')
    except socket.error as e:
        print(f"[-] Error during data transfer: {e}")
        return None
    
def main():
    """The main function that handles command-line arguments."""
    parser = argparse.ArgumentParser(
        description="A simple TCP client for connecting to a host and sending HTTP GET requests."
    )
    parser.add_argument("host", help="The host to connect to (e.g., www.google.com).")
    parser.add_argument("-p", "--port", type=int, default=80, help="the port to connect to (default: 80).")
    
    args = parser.parse_args()
    
    client_socket = create_client(args.host, args.port)
    if client_socket:
        response = send_and_receive(client_socket, args.host)
        if response:
            print("\n--- RECEIVED RESPONSE ---")
            print(response)
        client_socket.close()
if __name__ == "__main__":
    main()