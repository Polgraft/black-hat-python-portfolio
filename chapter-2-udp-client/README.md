# Chapter 3: Advanced UDP Client

This project is an enhanced version of the simple UDP client from the book "Black Hat Python: Python for Hackers and Pentesters" by Justin Seitz. It demonstrates fundamental networking concepts and their practical application in Python.

## What It Does

This script creates a basic UDP client that sends a message to a specified host and port. It then listens for a response from the server. It is a fundamental building block for more complex networking tools that rely on the connectionless UDP protocol.

## Key Learnings

* **Network Fundamentals**: Deepened my understanding of the **connectionless UDP protocol** and its key differences from TCP.
* **Robust Code Development**: Implemented **error handling** with `try...except` blocks to manage cases where no response is received (which is common for UDP).
* **Command-Line Argument Parsing**: Utilized the `argparse` module to create a flexible script that accepts dynamic host, port, and message inputs, a key feature for any useful security tool.
* **Code Modularity**: Refactored the code into a `main()` function for better readability and maintenance.

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/black-hat-python-portfolio.git](https://github.com/YourUsername/black-hat-python-portfolio.git)
    cd black-hat-python-portfolio/chapter-3-simple-udp-client
    ```

3.  **Run the script from the terminal, providing a host and optional port:**
    ```bash
    python3 udp_client.py 127.0.0.1 --port 9999 --message "Hello, world!"
    ```

## How to Run with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t simple-udp-client .
    ```
2.  **Run the container:**
    ```bash
    docker run simple-udp-client 127.0.0.1 --message "Hello, world!"
    ```

## Understanding the Dockerfile

This project includes a `Dockerfile` to create a portable and reproducible environment for the script. Using Docker demonstrates an understanding of modern software deployment practices.

The `Dockerfile` contains a series of instructions that automatically build a **Docker image**, which is a self-contained package of the application and all its dependencies.

### Key Benefits:

* **Portability**: The script will run the same way on any system (Linux, Windows, macOS) without compatibility issues.
* **Isolation**: It creates an isolated environment, preventing any conflicts with your host system's configuration or installed Python versions.
* **Dependency Management**: It ensures that all necessary libraries are included in the final package, making the project easy for others to use and test.
