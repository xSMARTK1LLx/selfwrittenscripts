import sys
import socket
from datetime import datetime
portcheck = [80, 443, 21, 22, 110, 995, 143, 993, 25, 26, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078]

#with open('C:\Users\Cyber Security\Downloads\1nt3rnR3p0rt5\2.txt') as f:
#with open('2.txt') as f:
#    target = [line.rstrip() for line in f]
#    target = f.readlines()
#myfile1 = open(r"C:\Users\Cyber Security\Downloads\1nt3rnR3p0rt5\2.txt","rt")
#target = "8.8.8.8" 

with open("2.txt", "r") as myfile1:
    for target in myfile1:
        target = target.strip()
        for port in portcheck:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #print(target,port)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
        #assert result == 0
            if result == 0:
                print("open" , target)
                break
        if result != 0:
            print("invalid", target)

"""
ips = ['193.169.10.100', '193.169.10.101']
ports = [80, 80]

for target in myfile1:
    try:
        for port in portcheck:
                #print('*')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
            if result ==0:
                break
        
    except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        #sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        #sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        #sys.exit()
"""

