import dpkt
import sys
from socket import *

def findDDos(pcap):
    pktcount = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet()
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport

            if dport == 80:
                stream = src + ":" + dst
                if pktCount.has_key(stream):
                    pktCount[stream] = pktCount[stream] + 1
                else:
                    pktCount[stream] = 1
        except:
            pass

    for stream in pktCount:
        pktsSent = pktCount[stream]
        if pktsSent > 10000:
            src = stream.split(":")[0]
            dst = stream.split(":")[1]
            print "[+] "+src+" attacked "+dst+" with "+str(pktsSent)+" pkts. "


try:
    pcapfile = sys.argv[1]
    f = open(pcapfile)
    pcap = dpkt.pcap.Reader(f)
    findDDos(pcap)
except:
    print "[!] usage : [pcapfile]"
    sys.exit(0)
