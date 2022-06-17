
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'virus.py' or file == 'thekey.key' or file == 'decrypt.py':
		continue
	if os.path.isfile(file):
		files.append(file)

with open('thekey.key', 'rb') as key:
	secret_key = key.read()
	
for file in files:
	with open(file, 'rb') as thefile:
		contents = thefile.read()
		decrypted_contents = Fernet(secret_key).decrypt(contents)
		with open(file, 'wb') as thefile:
			thefile.write(decrypted_contents)
print(files)
