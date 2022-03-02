import socket

# UDP socket connection to be used in try to response client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

msg_hello = 'Servidor: Hello client'
msg_bye = 'Servidor: Bye Bye client'

turnOn = True

server_socket.bind((host, port))

while turnOn:
    data, address = server_socket.recvfrom(4096)

    if data:

        data = data.decode()
        if data == 'turnoff server':
            print('Turn off server')
            turnOn = False
            server_socket.sendto(msg_bye.encode(), address)
        else:
            print('Server sending message...')
            server_socket.sendto(msg_hello.encode(), address)

server_socket.close()
