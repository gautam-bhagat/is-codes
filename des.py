from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_des(data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))
    return encrypted_data

def decrypt_des(encrypted_data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
    return decrypted_data

# Example usage:
key = get_random_bytes(8)  # 8 bytes key for DES
data = b"Hello, DES!"
encrypted_data = encrypt_des(data, key)
print("Encrypted data:", encrypted_data)
decrypted_data = decrypt_des(encrypted_data, key)
print("Decrypted data:", decrypted_data.decode())
