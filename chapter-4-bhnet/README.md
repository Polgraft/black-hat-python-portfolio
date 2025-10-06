# Chapter 4: `bhnet.py` — Multi-Purpose Netcat-like Tool

This project is a versatile network utility inspired by Netcat, combining a **TCP client** and a **multithreaded TCP server** in a single Python script. It is designed for learning and testing network communication and remote command execution.

> ⚠️ **Security & Ethics:** This tool can be used for both educational and malicious purposes. Only run it against systems you own or have explicit permission to test. Misuse may be illegal.

---

## What the Script Does

`bhnet.py` can operate in multiple modes, depending on CLI arguments:

* **Server Mode** — listens for incoming TCP connections, multithreaded to handle multiple clients.
* **Client Mode** — default mode; connects to a remote host and sends data.
* **Interactive Shell** — spawns a persistent remote shell on connection.
* **Execute on Connect** — executes a single system command and returns the output.
* **File Upload** — receives a file from a client and saves it to disk.

---

## Key Learnings

* **Dual-role networking** — switching logic between client and server modes.
* **Multithreading** — using `threading` to handle multiple clients concurrently.
* **Remote shell implementation** — maintaining session state, sending/receiving commands.
* **Safe command execution** — using `subprocess` and `shlex` to parse commands.
* **Error handling** — robust `try/except` blocks for network and system errors.
* **CLI arguments** — flexible usage through `argparse`.

---

## Modes & Examples

### General Syntax

```bash
python3 bhnet.py -t <target_host> -p <port> [flags]
```

### 1) Listener with Interactive Shell (Server)

Bind to all interfaces on port 9999:

```bash
python3 bhnet.py -t 0.0.0.0 -p 9999 -l -c
```

### 2) Execute a Single Command on Connection (Server)

Execute `whoami` and send the result to the client:

```bash
python3 bhnet.py -t 0.0.0.0 -p 4444 -l -e "whoami"
```

### 3) File Upload (Server)

Save received bytes to `/tmp/received.bin`:

```bash
python3 bhnet.py -t 0.0.0.0 -p 9000 -l -u /tmp/received.bin
```

### 4) Client Mode — Send Data or File

Send a file to a listening server:

```bash
cat ./localfile.bin | python3 bhnet.py -t 10.0.0.5 -p 9000
```

Interactive client connection:

```bash
python3 bhnet.py -t 192.168.1.10 -p 9999
```

---

## Running Locally

1. Make sure Python 3 (3.8+) is installed.
2. Clone the repository and go to Chapter 4:

```bash
git clone https://github.com/Polgraft/black-hat-python-portfolio.git
cd black-hat-python-portfolio/chapter-4-bhnet
```

3. Run the desired mode (examples above).

---

## Running in Docker

Build the image:

```bash
sudo docker build -t bhnet .
```

Run the container (mapping port 9999):

```bash
sudo docker run -p 9999:9999 --rm bhnet
```


