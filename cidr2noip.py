import ipaddress
from itertools import islice

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

with open("IPs_Scanned_Nov_21 - x.txt", "r") as myfile1:
    for target in myfile1:
        counter=0
        target = target.strip()
        if(validate_ip(target)):
            counter+=1
        #elif(validate_ip(target)):
        #    
        else:
            for ipadd in ipaddress.IPv4Network(target, strict=False):
                if(int(ipaddress.IPv4Address(ipadd)) >= int(ipaddress.ip_interface(target).ip)):
                    #print(str(ipadd))
                    counter+=1
        print("Cidr : ", target, " , No of IPs : ", counter)