import socket
import sys

if len(sys.argv) != 2:
    print("Usage: vrfy.py <username>")
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

baseAddr="10.11.1."
for ip in range(1,255):
    addr=baseAddr+str(ip)

    #Connect to SMTP
    try:
        connect=s.connect((addr,25))
    except socket.error as e:
        print(addr+" doesn't have SMTP open.")
        continue

    #Get the banner
    banner=s.recv(1024)
    print(banner)

    #VRFY a user
    s.send("VRFY " + sys.argv[1] +"\r\n")
    result=s.recv(1024)
    print result

s.close()
