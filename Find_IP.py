#!/usr/bin/python

####	Busca de IPs com porta especifica aberta
####	Mauricio Martins Donatti
####	mauricio.donatti@lnls.br
####	Ultima modificao: 08/05/2018

import socket

def get_name(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((addr,port))
    s.sendall("n\r")
    r = s.recv(1024)
    s.close()
    return r.split(" ")[-1]


network = '10.2.111.' #Search the last 255 addresses
port = 5757

def is_up(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.1)    ## set a timeout of 0.01 sec
    if not s.connect_ex((addr,port)):   # connect to the remote host on port 135
        s.close()                       ## (port 5757 is always open on Windows machines, AFAIK)
        return 1
    else:
        s.close()

def run():
    print ''
    for ip in xrange(1,256):    ## from addresses x.x.x.1 to x.x.x.255
        addr = network + str(ip)
        if is_up(addr):
            print("%s\t%s\t%s"%(addr,socket.getfqdn(addr),get_name(addr)))    ## the function 'getfqdn' returns the remote hostname
    print    ## just print a blank line


if __name__ == '__main__':

    run()
