from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data

def decrypt_aes(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    return decrypted_data

# Example usage:
key = get_random_bytes(16)  # 16 bytes key for AES-128
data = b"Hello, AES!"
encrypted_data = encrypt_aes(data, key)
print("Encrypted data:", encrypted_data)
decrypted_data = decrypt_aes(encrypted_data, key)
print("Decrypted data:", decrypted_data.decode())
