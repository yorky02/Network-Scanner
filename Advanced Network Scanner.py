import socket


# network scanner

def welcome():
    print('Welcome to the Advanced Network Scanner!')
    print("By Octavio Vieira")
    print()
welcome()

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

def single_port_scanner(ip, port):
    is_port_open(ip, port)
    try:
        if is_port_open(ip, port):
            print("Port is open")
        else:
            print("Port is closed")
    finally:
        print()
        print("thank you for using this tool !!!")

ip = input('Please enter ip address or hostname: ')
options = int(input('Select one of the following options: 1) Scan single port or 2) Scan multiple ports.'))

if options == 1:
    print()
    port = int(input("What port would you like to scan?: "))
    print()
    single_port_scanner(ip, port)
elif options == 2:
    print()
    print('This function is getting updated. Sorry!')
    print()
elif options != 1 and options != 2:
    print()
    print("Please enter a valid port. It must be an integer.")
    print()

#port = int(input("What port would you like to scan?: "))

#try:
    #port_scanning_type = int(input('Please enter port scanning type (number): '))
    #if port_scanning_type == port_scanning_type:
       # print(single_port_scanner(ip, port))
#except ValueError:
        #print("Please enter a valid port. It must be an integer.")





