import rsa

with open("keys/private.pem", 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

encrypted_message = open("encrypted_message.txt", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())