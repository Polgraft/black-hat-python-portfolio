# Chapter 3: Multithreaded TCP Server

This project is a multithreaded TCP server based on the examples from the book "Black Hat Python: Python for Hackers and Pentesters." It demonstrates my understanding of foundational networking concepts and their practical application in Python.

## What It Does

This script creates a robust TCP server that listens for incoming connections. For each new client, it spawns a dedicated thread to handle communication, ensuring the server can manage multiple concurrent connections without blocking. It receives a message from the client and sends a simple "ACK!" response back.

## Key Learnings

* **Network Fundamentals**: Deepened my understanding of the **TCP three-way handshake**, client-server communication, and the role of server sockets.
* **Multithreading**: Implemented **`threading`** to handle multiple clients concurrently, a crucial skill for building high-performance network applications.
* **Robust Code Development**: Utilized the **`argparse`** module to accept host and port inputs from the command line, making the server flexible and reusable.
* **Code Modularity**: Structured the code into distinct functions (`main` and `handle_client`) for improved readability and maintenance.

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/Polgraft/black-hat-python-portfolio.git
    cd black-hat-python-portfolio/chapter-3-tcp-server
    ```
3.  **Run the server from the terminal, providing a host and optional port:**
    ```bash
    python3 tcp.server.py 0.0.0.0 --port 9998
    ```
    *The server will start listening for connections.*

## How to Run with Docker

1.  **Build the Docker image:**
    ```bash
    sudo docker build -t tcp.server .
    ```
2.  **Run the container:**
    ```bash
    sudo docker run -p 9998:9998 tcp.server
    ```
    *The server will now be running inside the container and listening on your host's port 9998.*
