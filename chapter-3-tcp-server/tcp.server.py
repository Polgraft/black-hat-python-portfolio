import socket
import threading
import argparse

def handle_client(client_socket):
    """
    Handles client requests by receiving data and sending a response.
    This function runs in a seperate thread for each client.
    """
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8', 'ignore')}")
        sock.send(b'ACK!')
        
def main():
    """
    Sets up and runs the main TCP server logic.
    """
    # Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="A simple multithreaded TCP server."
    
    )
    parser.add_argument("host", default="0.0.0.0", nargs='?', help="The IP address to listen on (default: 0.0.0.0).")
    parser.add_argument("-p", "--port", type=int, default=9998, help="the port to listen on (default: 9998).")
    
    args = parser.parse_args()
    
    # Create the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((args.host, args.port))
    server.listen(5)
    
    print(f'[*] Listening on {args.host}:{args.port}')
    
    # The main loop to accept incoming client connections
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
if __name__ == "__main__":
    main()
                                          
    