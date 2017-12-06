import paramiko
import sys

try:
    ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
except:
    print "Usage: [ip] [username] [password]"
    sys.exit(0)

def ssh_command(ip, user, passwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=passwd)
        sessions = client.get_transport().open_session()

        if sessions.active:
            command = raw_input("Enter command:")
            sessions.exec_command(command)
            print(sessions.recv(65565))
    except KeyboardInterrupt:
        sys.exit(0)
    
    return 

ssh_command(ip, username, password)

