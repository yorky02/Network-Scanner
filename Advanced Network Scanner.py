import socket

# network scanner

def is_port_open(ip, port):
    port_checker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_checker.settimeout(3)
    condition_helper = port_checker.connect_ex((ip, port))

    try:
        if condition_helper == 0:
            return True
        elif condition_helper != 0:
            return False
    finally:
        port_checker.close()

is_port_open('localhost', 7000)

ports = []

for port in range(1, 7001):
    if is_port_open('localhost', port):
        ports.append(port)
print('The following ports are open:', ports)


