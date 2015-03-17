#!/usr/bin/local python
import socket
import subprocess

def banner():
	subprocess.call('cls', shell=True)
	subprocess.call('color b', shell=True)
	print("# "*25)
	print("#    -= Basic P0rt Sc4Nn3r by diego1996 =-        #")
	print("#                @Diego_Asencio                 #")
	print("# "*25)

def estaAbierto(host, port):
	s = socket.socket()
	res = s.connect_ex((host, port))
	if res == 0:
		return True
	else:
		return False
		
def main():
	print("."*25)
	host = input("Ingrese una direccion IP : ")
	print("RAGNOS PARA REALIZAR EL SCANN")
	x1 = input("Desde: ")
	x2 = input("Hasta: ")
	print("-"*25)
	print("Scanneando puertos en host: " +str(host))
	print("-"*25)
	for port in range(int(x1), int(x2)+1):
		if estaAbierto(str(host), port) :
			print("[+] Puerto "+ str(port) + " Abierto")
		else:
			print("[-] Puerto "+str(port) + " Cerrado")

banner()
main()
