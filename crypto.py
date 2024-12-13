from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random key
key = os.urandom(32)

# Generate a random initialization vector (IV)
iv = os.urandom(16)

# Create an AES cipher object
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

# Encrypt a message
message = b"hello,world!"
padder = padding.PKCS7(128).padder()
padded_message = padder.update(message) + padder.finalize()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

# Decrypt the message
unpadder = padding.PKCS7(128).unpadder()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()
unpadded_message = unpadder.update(decrypted_padded_message)
unpadded_message += unpadder.finalize()

print(unpadded_message.decode())  # Output: Hello, World!
