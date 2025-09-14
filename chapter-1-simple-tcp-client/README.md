# Chapter 1: Advanced TCP Client

This project is an enhanced version of the simple TCP client from the book "Black Hat Python: Python for Hackers and Pentesters" by Justin Seitz. It demonstrates foundational networking concepts and their practical application in Python.

## What It Does

This script creates a basic TCP client that connects to a specified host and port. It then sends a standard HTTP GET request and prints the server's response. It is a fundamental building block for more complex networking tools like port scanners or web crawlers.

## Key Learnings

* **Network Fundamentals**: Deepened my understanding of the **TCP three-way handshake** and how client-server communication works at a low level.
* **Robust Code Development**: Implemented **error handling** with `try...except` blocks to manage connection failures and network errors.
* **Command-Line Argument Parsing**: Utilized the `argparse` module to create a flexible script that accepts dynamic host and port inputs, a key feature for any useful security tool.
* **Code Modularity**: Refactored the code into reusable functions (`create_client`, `send_and_receive`) for better readability and maintenance.

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Polgraft/black-hat-python-portfolio.git](https://github.com/YourUsername/black-hat-python-portfolio.git)
    cd black-hat-python-portfolio/chapter-1-simple-tcp-client
    ```
3.  **Run the script from the terminal, providing a host and optional port:**
    ```bash
    python3 tcp_client.py [www.google.com](https://www.google.com) --port 80
    ```

### How to Run with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t simple-tcp-client .
    ```
2.  **Run the container:**
    ```bash
    docker run simple-tcp-client [www.google.com](https://www.google.com)
    ```
## Understanding the Dockerfile

This project includes a `Dockerfile` to create a portable and reproducible environment for the script. Using Docker demonstrates an understanding of modern software deployment practices.

The `Dockerfile` contains a series of instructions that automatically build a **Docker image**, which is a self-contained package of the application and all its dependencies.

### Key Benefits:

* **Portability**: The script will run the same way on any system (Linux, Windows, macOS) without compatibility issues.
* **Isolation**: It creates an isolated environment, preventing any conflicts with your host system's configuration or installed Python versions.
* **Dependency Management**: It ensures that all necessary libraries are included in the final package, making the project easy for others to use and test.
