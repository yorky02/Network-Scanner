# Python Network Scanner

A Python-based TCP network scanner built using socket programming.

This project scans ports on a target IP address or hostname and reports open ports and common network services. The scanner supports single-port scans, custom port-range scans, common-port quick scans, and exporting scan results to a text file.

## Features

- Single port scanning
- Custom port range scanning
- Common-port quick scan
- Service name mapping
- Scan result exporting
- Port validation
- TCP socket connections

## Technologies Used

- Python
- Socket programming
- Debian Linux
- Git/GitHub

## Example Services Detected

| Port | Service |
|------|----------|
| 21 | FTP |
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |

## How to Run

Clone the repository:

```bash
git clone https://github.com/yorky02/python-network-scanner.git
```

Go into the project folder:

```bash
cd python-network-scanner
```

Run the scanner:

```bash
python3 scanner.py
```

## Example Usage

```text
Select option:
1) Scan single port
2) Scan multiple ports
3) Quick scan (common ports)
```

## Future Improvements

- Multithreaded scanning
- Hostname resolution
- Command-line arguments
- Banner grabbing
- Improved logging
- Better error handling

## What I Learned

This project helped me improve my understanding of:

- TCP/IP networking
- Ports and common services
- Python socket programming
- Linux command-line workflow
- Input validation
- File handling
- Network troubleshooting basics

## Disclaimer

This project is intended for educational purposes and authorized testing only.
