## <p align="center" style="font-size: 32px; font-weight: bold;">ArtemisShell</p>

ArtemisShell is a powerful, lightweight, and versatile bi-directional reverse shell tool. It enables secure and efficient communication between two devices, allowing both the server and client to send commands and receive output. this tool aims to provide users with a streamlined solution for establishing remote command execution channels.

<br>

<p align="center">
  <img src="./artemis.png" alt="ArtemisShell Logo">
</p>

<br>

## Features <br>

- Bi-directional communication: Enables both the server and client to send commands and receive output.
- Lightweight and efficient: Minimal resource usage and fast execution.
- Simple setup: Easy to configure and get started quickly.
- Cross-platform compatibility: Works on various operating systems, including Windows, macOS, and Linux.

## Use Cases <br>
ArtemisShell is suitable for various applications, including: <br>

- Penetration testing: Assess and exploit security vulnerabilities in remote systems. <br>
- System administration: Manage and troubleshoot remote systems effectively. <br>
- Development and debugging: Collaborate and debug applications on remote machines.


## Installation
Clone the repository:
``` bash
git clone https://github.com/blue0x1/ArtemisShell

```
Change to the project directory:
 
``` bash 
cd ArtemisShell
```

Ensure you have Python 3 installed on your system. <br>
## Usage
Start the server:

``` bash
python3 Artemis.py  --mode server --ip [server-ip] --port [port-number]
```
Start the client: 

``` bash

python3 Artemis.py  --mode client --ip [server-ip] --port [port-number]
```
<br>
Send commands from either the server or client by typing them into the terminal and pressing Enter.

To close the connection, press Ctrl+C or type exit in the terminal.
<br>




