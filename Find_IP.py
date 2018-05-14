#!/usr/bin/python

####	Busca de IPs com porta especifica aberta
####	Mauricio Martins Donatti
####	mauricio.donatti@lnls.br
####	Ultima modificao: 08/05/2018

import socket
import re

#network = '10.2.111.' #network subdomain will be prompted
port = 6767

def get_name(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    s.connect_ex((addr,port))
    s.sendall("n?\r")
    r = s.recv(1024)
    s.close()
    return r.split(" ")[-1]

def is_up(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.05)    ## set a timeout of 0.05 sec
    if not s.connect_ex((addr,port)):   # connect to the remote host on port 6767
        s.close()
        return 1
    else:
        s.close()

def run():
    print ''
    for ip in xrange(1,256):    ## from addresses x.x.x.1 to x.x.x.255
        addr = network + "." + str(ip)
        if is_up(addr):
            print("%s\t%s\t%s"%(addr,socket.getfqdn(addr),get_name(addr)))    ## the function 'getfqdn' returns the remote hostname
    print    ## just print a blank line


if __name__ == '__main__':
    network = raw_input("Enter the network subdomain: ")

    try:
        parts = network.split('.')
        if len(parts) == 3 and all(0 <= int(part) < 256 for part in parts):
            run()
        else:
            raise TypeError
    except (AttributeError, TypeError,ValueError):
        print("IP subdomain Not valid")
