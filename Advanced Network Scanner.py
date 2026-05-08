import socket

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Alternate"
}

def welcome():
    print("Welcome to the Advanced Network Scanner!")
    print("By Octavio Vieira")
    print()


def is_port_open(ip, port):
    port_checker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_checker.settimeout(0.5)

    try:
        result = port_checker.connect_ex((ip, port))

        if result == 0:
            return True
        else:
            return False

    finally:
        port_checker.close()


def single_port_scanner(ip, port):
    if is_port_open(ip, port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")


def multiple_port_scanner_range(ip, start_port, end_port):
    open_ports = []

    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if is_port_open(ip, port):
            open_ports.append(port)
            print(f"Port {port} is open")

    print("\nScan complete.")

    if len(open_ports) > 0:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

    return open_ports

def common_port_scanner(ip):

    common_ports = [21, 22, 25, 53, 80, 443, 8080]

    open_ports = []

    for port in common_ports:
        if is_port_open(ip, port):
            open_ports.append(port)
            print(f"Port {port} is open")

    print("\nScan complete.")

    if len(open_ports) > 0:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

    return open_ports

def valid_port(port):
    return port >= 1 and port <= 65535

def export_results(open_ports):
    with open("Scan-results.txt", "a") as file:
        file.write("Port Scanning Results:\n")

        for port in open_ports:
            service = COMMON_PORTS.get(port, "Unknown service")
            file.write("Port " + str(port) + " is open. Currently running: " + service + "\n")
        file.write("\n")

def main():
    welcome()

    ip = input("Please enter IP address or hostname: ")

    try:
        options = int(input("Select option: 1) Scan single port or 2) Scan multiple ports or 3) Quick scan (common ports):  "))

        if options == 1:
            port = int(input("What port would you like to scan?: "))

            if valid_port(port):
                single_port_scanner(ip, port)
            else:
                print("Port must be between 1 and 65535.")

        elif options == 2:
            start_port = int(input("Please enter the starting port number: "))
            end_port = int(input("Please enter the ending port number: "))

            if valid_port(start_port) and valid_port(end_port) and start_port <= end_port:
                open_ports = multiple_port_scanner_range(ip, start_port, end_port)
                export_result = input("Would you like to export results (y/n): ")
                if export_result == "y":
                    export_results(open_ports)
                else:
                    print("Exiting...")
            else:
                print("Invalid range. Ports must be between 1 and 65535, and start must be <= end.")
        elif options == 3:
            print(f"\nScanning {ip} from common ports...\n")
            open_ports = common_port_scanner(ip)
            export_result = input("Would you like to export results (y/n): ")
            if export_result == "y":
                export_results(open_ports)
        else:
            print("Please enter a valid option: 1 or 2, or 3.")

    except ValueError:
        print("Please enter numbers only for options and ports.")

    print("\nThank you for using this tool!")


main()