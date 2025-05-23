# py-nmap

A simple Python wrapper for the Nmap network scanning tool.

## Description

This project provides a Python interface for running Nmap scans and parsing the results. It allows you to easily identify hosts and open ports on a network.

## Project Structure

The repository is organized as follows:

- **src/**: Contains the main source code
  - `main.py`: Main script for running Nmap scans
  - `__init__.py`: Package initialization file

## Features

- Scan IP addresses to identify open ports
- Display results in a readable format
- Simple and intuitive command-line interface

## Usage Example

The main script allows you to run a basic scan:

```python
import nmap

scanner = nmap.PortScanner()

ip = input("❗ Enter the IP address you want to scan: ")
print(f"🔎 Scanning {ip} for open ports...")

scanner.scan(ip, arguments='-p-')

for host in scanner.all_hosts():
    print(f"🌐 Host: {host}")
    print(f"💻 Open ports: {list(scanner[host]['tcp'].keys())}")
```

## Requirements

To use this project, you need to install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Additionally, you need to have Nmap installed on your system.

## Installing Nmap

### Windows

1. Download Nmap from [nmap.org](https://nmap.org/download.html)
2. Run the installer and follow the instructions

### Linux
```bash
sudo apt-get install nmap  # Debian/Ubuntu
sudo yum install nmap      # CentOS/RHEL
```

### macOS
```bash
brew install nmap
```

## How to Run

To start the script:

```bash
python src/main.py
```

When prompted, enter the IP address you want to scan.

## Security Warnings

- Only use this tool on networks for which you have permission to scan
- Unauthorized port scanning may be illegal in some jurisdictions
- This tool is intended for educational and legitimate network administration purposes only

## License

This project is distributed under an open source license. See the LICENSE file for more details.

---

*This project was created as a practical exercise on network security tools.*