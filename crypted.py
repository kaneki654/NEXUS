import threading
import bcrypt
import sys
import os



file = open('10-million-password-list-top-1000000.txt', 'r') #This is your wordlist
lines = file.readlines()
 


def brute():
	passwdstr=line.strip()
	passwd =passwdstr.encode('UTF-8')
	salt=b'' #It doesn't matter, so don't change.
	hashed = b'$2y$10$drphlgMqp5v9eCIiGaA0oeaQdNst0W4taMvhbtWM2e9nRZlB' #your bcrypt hash here.
	if bcrypt.checkpw(passwd, hashed):
		print(f"Hash Cracked Successfully. Your Password is {passwdstr}.......................................\n")
		os._exit(0)
		print()
	else:
		sys.stdout.write(f"{passwdstr} does not match this hash.{c} passwords tried so far. \033[0m\033[0K\r")
		


threads = []




c= 0
for line in lines:
	c += 1
	thread = threading.Thread(target = brute)
	thread.start()
	threads.append(thread)


for thread in threads:
   	thread.join()
   