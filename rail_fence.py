def encrypt_rail_fence(plaintext, key):
    ciphertext = [''] * len(plaintext)
    rail = [''] * key
    direction = -1
    row = 0
    
    for char in plaintext:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction *= -1
        row += direction
    
    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            ciphertext[index] = rail[i][j]
            index += 1
    
    return ''.join(ciphertext)

def decrypt_rail_fence(ciphertext, key):
    plaintext = [''] * len(ciphertext)
    rail = [''] * key
    direction = -1
    row = 0
    
    for char in ciphertext:
        rail[row] += '*'
        if row == 0 or row == key - 1:
            direction *= -1
        row += direction
    
    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            rail[i] = rail[i][:j] + ciphertext[index] + rail[i][j+1:]
            index += 1
    
    row = 0
    direction = -1
    for i in range(len(ciphertext)):
        plaintext[i] = rail[row][0]
        rail[row] = rail[row][1:]
        if row == 0 or row == key - 1:
            direction *= -1
        row += direction
    
    return ''.join(plaintext)

# Example usage:
plaintext = "Hello World"
key = 3
encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted text:", decrypted_text)
