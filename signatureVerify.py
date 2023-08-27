import rsa

public_key, private_key = rsa.newkeys(1024) # 1024 bytes

#Creating public Key
with open('keys/public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1("PEM"))

# Creating Private Key
with open('keys/private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1("PEM"))

message = "I have a demat account where i put all my Bitcoins and the address is @madeupname19980803"


with open('signature', "rb") as f:
    signature = f.read()


verify = rsa.verify(message.encode(), signature, public_key)

print(verify)