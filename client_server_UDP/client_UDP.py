import socket

# UDP socket connection to be used in try to connect the local server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

msg = 'Hello server'
msg_offServer = 'turnoff server'

try:
    print(f'Client: {msg}')

    # Sending message to local server
    client_socket.sendto(msg.encode(), (host, port))

    data, server = client_socket.recvfrom(4096)

    data = data.decode()
    print(data)
finally:
    print('Client: Closing connection and turn off server')

    client_socket.sendto(msg_offServer.encode(), (host, port))
    data, server = client_socket.recvfrom(4096)

    data = data.decode()
    print(data)

    client_socket.close()
