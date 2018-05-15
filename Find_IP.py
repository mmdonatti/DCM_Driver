#!/usr/bin/python

####	Search for IPs on a subdomain with an open TCP socket port
####	Mauricio Martins Donatti
####	mauricio.donatti@lnls.br
####	Brazilian Synchrotron Light Laboratory

import socket

#network = '10.2.111.' #network subdomain will be prompted
port = 6767     #Driver Heaters TP port

#get device name
def get_name(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #init Socket
    s.settimeout(1)                                         #set 1 second timeout
    s.connect_ex((addr,port))                               #try to connect
    s.sendall("n?\r")                                       #ask device name
    r = s.recv(1024)                                        #receive answer
    s.close()                                               #close socket
    return r.split(" ")[-1]                                 #split and take the last string

#verify if a device with "port" is ready
def is_up(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #init Socket
    s.settimeout(0.05)                                      ## set a timeout of 0.05 sec
    if not s.connect_ex((addr,port)):                       # connect to the remote host on port 6767
        s.close()                                           # if succesfull clsoe socket and return 1
        return 1
    else:
        s.close()                                           #only close socket (no server response)

#main function
def run():
    print("")
    for ip in xrange(1,256):                ## from addresses x.x.x.1 to x.x.x.255
        addr = network + "." + str(ip)      ## generate address list
        if is_up(addr):                     ##if device is up
            print("%s\t%s\t%s"%(addr,socket.getfqdn(addr),get_name(addr)))    ## the function 'getfqdn' returns the remote hostname and get_name the protocol name
    print("")

if __name__ == '__main__':
    network = raw_input("\nEnter the network subdomain (format XXX.XXX.XXX): ")      #Network domain must be in format XXX.XXX.XXX

    try:    #Verify if network is a valid neetwork subdomain
        parts = network.split('.')
        if len(parts) == 3 and all(0 <= int(part) < 256 for part in parts): #3 parts, all between 0 and 255
            run()
        else:
            raise TypeError
    except (AttributeError,TypeError,ValueError):
        print("IP subdomain not valid")
