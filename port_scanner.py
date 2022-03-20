import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input('Enter the IP address to scan: ')
port = int(input('Enter the PORT to scan: '))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is opened")

portScanner(port)