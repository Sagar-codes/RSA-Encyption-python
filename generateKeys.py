import rsa
import os

public_key, private_key = rsa.newkeys(1024) # 1024 bytes


parent_dir = os.getcwd()
keys_directory = "keys"

path = os.path.join(parent_dir, keys_directory)
os.mkdir(path)

#Creating public Key
with open('keys/public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1("PEM"))

# Creating Private Key
with open('keys/private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1("PEM"))
