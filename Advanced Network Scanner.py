import socket


# network scanner

def welcome():
    print('Welcome to the Advanced Network Scanner!')
    print("By Octavio Vieira")
    print()

def is_port_open(ip, port):
    port_checker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_checker.settimeout(0.5)
    condition_helper = port_checker.connect_ex((ip, port))

    try:
        if condition_helper == 0:
            return True
        elif condition_helper != 0:
            return False
    finally:
        port_checker.close()

def ask_user():
    ip = input('Please enter ip address or hostname: ')
    print(ip)
    print()
    print('Select one of the following options: 1) Scan single port or 2) Scan multiple ports.')
    while True:
        try:
            port_scanning_type = int(input('Please enter port scanning type (number): '))
            port = int(input("What port would you like to scan?: "))
            if port_scanning_type == 1:
                print(port)
            elif is_port_open(ip, port):
                print("Port is open")
            else:
                print("Port is closed")
        except ValueError:
                print("Please enter a valid port. It must be an integer.")

    #single_or_multiple_ports = input('Would you like to scan for multiple ports (y/n): ')
    #if single_or_multiple_ports.lower() == 'y':
        #print('Scanning for open ports...')

        #ports = []

        #for port in range(1, 1025):
            #if is_port_open(ip, port):
                #ports.append(port)
        #print('Open ports:', ports)

    #elif single_or_multiple_ports.lower() == 'n':

        #try:
            #port = int(input("What port would you like to scan?: "))
            #if is_port_open(ip, port):
                #print("Port is open")
            #else:
                #print("Port is closed")
        #except ValueError:
            #print("Please enter a valid port. It must be an integer.")
            #ask_user()

welcome()
ask_user()


