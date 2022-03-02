import os
import socket
import sys

# reading host's file
with open('hosts.txt') as file:
    hosts = file.readlines()

# remove \n in list's items, although to be not need
hosts = list(map(lambda host: host.strip(), hosts))

# split each item by ';' creating a list of lists with host and his port
hosts = list(map(lambda host: host.split(';'), hosts))
print(hosts)

# pinging each item
for host in hosts:
    print("*" * 50)

    print(f'Ping at {host[0]} \n')
    os.system(f'ping -n 2 {host[0]}')

    print("*" * 50)

    # TCP socket connection to be used in try to connect each host at host's list
    # Necessary create a socket for each try of connection
    # It hasn't relation with ping above
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Socket's connection couldn't be done")
        print(e)
        continue

    try:
        # Tuple with host and port of host's list
        client_socket.connect((host[0], int(host[1])))
        print('Connection with this host OK.')
    except socket.error as e:
        print("Connection couldn't be done with this host.")
        print(e)

    client_socket.close()
