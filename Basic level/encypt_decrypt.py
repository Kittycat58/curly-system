from cryptography.fernet import Fernet

# Generate a random key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Message to be encrypted
message = "This is a secret message"

# Encrypt the message
cipher_text = cipher_suite.encrypt(message.encode())
print("Encrypted Text:", cipher_text)

# Decrypt the message
decipher_text = cipher_suite.decrypt(cipher_text)
print("Decrypted Text:", decipher_text.decode())
