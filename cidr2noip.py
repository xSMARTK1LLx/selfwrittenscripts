import ipaddress
from itertools import islice
char1 = set('-')
char2 = set(' ')

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
        
        if any((c in char1) for c in target):
            if any((c in char2) for c in target):
                ipranges = target.split(" - ")
                #print(ipranges[0])
                for numbcount in range(int(ipaddress.IPv4Address(ipranges[0])), int(ipaddress.IPv4Address(ipranges[1]))+1):
                    counter+=1
            else:
                ipranges = target.split("-")
                ippartfull = ipranges[0].split(".")
                ippart1 = int(ippartfull[3])
                ippart2 = int(ipranges[1])
                if(ippart1<=ippart2):
                    counter = ippart2-ippart1+1
                
        elif(validate_ip(target)):
            counter+=1
        
        else:
            for ipadd in ipaddress.IPv4Network(target, strict=False):
                if(int(ipaddress.IPv4Address(ipadd)) >= int(ipaddress.ip_interface(target).ip)):
                    #print(str(ipadd))
                    counter+=1
        print("Cidr : ", target, " , No of IPs : ", counter)
