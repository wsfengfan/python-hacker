import socket
import os 
import sys
from ctypes import *
import struct

class IP(Structure):
    _fields_ = [("inl", c_ubyte, 4),("version", c_ubyte, 4),("tos", c_ubyte),("len", c_ushort),("id", c_ushort),("offset", c_ubyte),("protocol_num", c_ubyte),("sum", c_ushort),("src", c_ulong),("dst", c_ulong)]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.protocol_map = {1:'ICMP', 6:'TCP', 17:'UDP'}

        self.src_address = socket.inet_ntoa(struct.pack('<L', self.src))
        self.dst_address = socket.inet_ntoa(struct.pack('<L', self.dst))

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

try:
    host = sys.argv[1]
    encodeIP = True
    encodeIP = sys.argv[2]
except:
    print "[!] Usage: [ip] [encode:True and False]"

try:
    if os.name == "nt":
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    sock.bind((host, 0))

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == "nt":
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while True:
        try:
            if encodeIP == True:
                sock_buffer = sock.recvfrom(65565)[0]
                ip_header = IP(sock_buffer[0:20])
                print "Protocol: %s:%s -> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)
            else:
                print sock.recvfrom(65565)
        except KeyboardInterrupt:
            print "[*] KeyboardInterrupt Stop..."
            sys.exit(0)

    if os.name == "nt":
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

except:
    print "[*] Stop..."
    sys.exit(0)
