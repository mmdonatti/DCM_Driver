#!/usr/bin/python

####	Comunicacao com driver heaters DCM
####	Mauricio Martins Donatti
####	mauricio.donatti@lnls.br
####	Ultima modificao: 14/05/2018

import socket
import datetime
import os.path
import time
import sys

ip = '10.2.111.42' 		#raw_input("Qual IP para comunicacao?\n")
porta = 6767 			#raw_input("Qual porta para comunicacao Telnet?\n")

print("O ip e : %s . A porta e %d " %( ip, porta))

menu = {}
menu['r']=" - Read Variables"
menu['l']=" - Current Limit"
menu['e']=" - Enable"
menu['ping']=" - Ping message"
menu['v']=" - Return Firmware Version"
menu['n']=" - Return Device Name"
menu['reset']=" - Reboot device"
menu['q']=" - Quit"

server_address=(ip,porta)

def send_socket(socket,str):
	socket.connect(server_address)
	socket.sendall(str)
	r = s.recv(1024)
	s.close()
	return r



try:
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		options=menu.keys()
		options.sort()
		not_open = 0
		for entry in options:
			print(entry, menu[entry])
		selection=raw_input("\nPlease Select:")
		if selection =='q':
			raise SystemExit
		elif (selection in ['ping','v']):
			print "No Parameter Command"
			ans = send_socket(s,selection+"\r")
			print "Answer: " + ans
		elif (selection == 'reset'):
			print "No Parameter Command"
			ans = send_socket(s,selection+"\r")
			print "Answer: " + ans
			raise SystemExit
		elif selection == 'r':
			channel=raw_input("\nEnter Channel\n")
			ans = send_socket(s,channel+selection+"\r")
			print "Answer: " + ans
		elif selection == 'n':
			param=raw_input("\nSET (s) ou GET (g)?\n")
			if (param in ['s','S','set','SET','Set']):
				param="="+raw_input("\nEnter device name to set\n")+"\0"
			else:
				param = "?"
			ans = send_socket(s,selection+param+"\r")
			print "Answer: " + ans
		elif (selection in ['l','e']):
			channel=raw_input("\nEnter Channel\n")
			print "Parameter Command\n"
			param=raw_input("\nSET (s) ou GET (g)?\n")
			if (param in ['s','S','set','SET','Set']):
				param=raw_input("\nDigite o valor do parametro: \n")
				if selection == 'l':
					param = str("%3.2f"%float(param))
				ans = send_socket(s,channel+selection + param+"\r")
				print "Answer: " + ans
			elif (param in ['g','G','get','GET','Get']):
				ans = send_socket(s,channel+selection+"?\r")
				print "Answer: " + ans
		else:
			print "Unknown Option Selected!"
except (KeyboardInterrupt,EOFError,SystemExit):
	print("Closing Program")

except (socket.timeout):
	print("Socket Timeout")
