import rsa

with open("keys/public.pem", 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

message = "Hello My Name is Sagar Paul, And I am Software Developer"

encrypted_message = rsa.encrypt(message.encode(), public_key)

with open("encrypted_message.txt.", "wb") as f:
    f.write(encrypted_message)
