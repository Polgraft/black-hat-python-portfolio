import socket
import sys
import argparse

def main():
    # Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="A simple UDP client to send a message to a host."
    )
    parser.add_argument("host", help="The host to send the message to.")
    parser.add_argument("-p", "--port", type=int, default=9999, help="The port to use (default: 9999).")
    parser.add_argument("-m", "--message", default="Hello, World!", help="The message to send (default: 'Hello, World!').")

    args = parser.parse_args()

    # Create a UDP socket
    # AF_INET = IPv4 protocol
    # SOCK_DGRAM = UDP protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send data (the message) to the specified host and port
    print(f"[*] Sending message to {args.host}:{args.port}")
    message_bytes = args.message.encode('utf-8')
    client.sendto(message_bytes, (args.host, args.port))

    # Receive a response
    try:
        # Set a timeout for 5 seconds to prevent the script from hanging indefinitely
        client.settimeout(5)
        response, addr = client.recvfrom(4096)
        print(f"[*] Received response from {addr[0]}:{addr[1]}")
        print(f"[*] Response: {response.decode('utf-8')}")
    except socket.timeout:
        print("[-] No response received. The server may be down or the message was lost.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    finally:
        # Always close the socket to free up resources
        client.close()

if __name__ == "__main__":
    main()