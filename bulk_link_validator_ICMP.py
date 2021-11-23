from ping3 import ping

#value = ping('google.co.in')
myfile1 = open(r"C:\Users\Cyber Security\Downloads\1nt3rnR3p0rt5\2.txt","rt")

for line in myfile1:
    urls = ping(line)
#    print(line)
    if urls == False or urls == None:
        print(str(line)+' doesnt exist.')
    else:
        print(str(line)+' exist.')
    
#print(value)


#if value == False or value == None:
#    print("doesn't exist")
#else:
#    print("exists")
myfile1.close()
