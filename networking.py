import socket

HOST = 'DESKTOP-708A91K'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

# Praveen's public IP - 192.168.1.3
# name: DESKTOP-Q8UUSGD
# My Desktop name - DESKTOP-708A91K
# My public IP - 192.168.0.103