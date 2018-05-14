#!/usr/bin/python

####	Busca de IPs com porta especifica aberta 		
####	Mauricio Martins Donatti			
####	mauricio.donatti@lnls.br				
####	Ultima modificao: 08/05/2018	

import socket

from socket import *
network = '10.2.111.' #Search the last 255 addresses
port = 5757

def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.2)    ## set a timeout of 0.01 sec
    if not s.connect_ex((addr,port)):    # connect to the remote host on port 135
        s.close()                       ## (port 135 is always open on Windows machines, AFAIK)
        return 1
    else:
        s.close()

def run():
    print ''
    for ip in xrange(1,256):    ## from addresses x.x.x.1 to x.x.x.255
        addr = network + str(ip)
        if is_up(addr):
            print '%s \t- %s' %(addr, getfqdn(addr))    ## the function 'getfqdn' returns the remote hostname
    print    ## just print a blank line


if __name__ == '__main__':

    run()