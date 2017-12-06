from socket import *
import sys
from datetime import datetime

def scannt(ip, port):
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.settimeout(1)
    try:
        tcp_sock.connect((ip, port))
        print("%d port ------ OPEN"%port)
    except:
        return
    

if __name__ == "__main__":

    try:
        ip = sys.argv[1]
        print("[*] Target:%s"%ip)
        print("[*] Sweep starting...")
    except:
        print "[!] Usage: [target IP]"
        sys.exit(0)

    t = datetime.now()
    portary = [7,9,13,21,22,25,37,53,79,80,88,106,110,113,119,135,139,143,179,199,389,427,443,444,465,513,514,543,548,554,587,631,646,873,990,993,995,1025,1026,1027,1028,1110,1433,1720,1723,1755,1900,2000,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000,6646,7070,8000,8008,8080,8443,8888,9100,9999,32768,49152,49153,49154,49155,49156]
        
    for port in portary:
        scannt(ip, port)

    t1 = datetime.now()
    t2 = t1 - t 
    print("[*] End of scan")
    print("[*] Multiprocess Scanning Completed in %s"%t2)
