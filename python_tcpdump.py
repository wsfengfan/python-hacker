import sys
from socket import *

def server_listen(localhost_ip, localhost_port, remote_ip, remote_port):
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind((localhost_ip, localhost_port))
    except:
        print "[!] Check for other listening sockets or correct permissions."
        sys.exit(0)

    server.listen(5)

    while True:
        local_socket, addres = server.accept()
        print "[*] Received incoming connection from %s:%d" % (addres[0], addres[1])

        target_socket = threading.Thread(target=target_client, args=(localhost_ip, localhost_port, remote_ip, remote_port, local_socket))
        target_socket.start()


def target_client(localhost_ip, localhost_port, remote_ip, remote_port, local_socket):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((remote_ip, remote_port))

    while True:
        local_buffer = local_socket.recv(65565)
        if len(local_buffer):
            client_socket.send(local_buffer)
            print "[*] send to remote_ip..."
            print local_buffer

        remote_buffer = client_socket.recv(65565)
        if len(remote_buffer):
            local_socket.send(remote_buffer)
            print "[*] send to localhost_ip..."
            print remote_buffer

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            local_socket.close()
            print "[*] No more data. Closing connections."

            sys.exit(0)

try:
    localhost_ip = sys.argv[1]
    localhost_port = sys.argv[2]

    remote_ip = sys.argv[3]
    remote_port = sys.argv[4]
    server_listen(localhost_ip, localhost_port, remote_ip, remote_port)
except:
    print "Usage: [localhost_ip] [localhost_port] [remote_ip] [remote_port]"

    
