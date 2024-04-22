def prepare_text(text):
    text = text.upper().replace("J", "I")  # Replace 'J' with 'I' and convert to uppercase
    text = ''.join(filter(str.isalpha, text))  # Remove non-alphabetic characters
    return text

def generate_key_square(key):
    key = prepare_text(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = ""
    for char in key:
        if char not in key_square:
            key_square += char
    for char in alphabet:
        if char not in key_square:
            key_square += char
    return key_square

def generate_pairs(text):
    text = prepare_text(text)
    pairs = []
    i = 0
    while i < len(text):
        pair = text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                pair += 'X'
                i -= 1
            else:
                pair += text[i + 1]
        else:
            pair += 'X'
        pairs.append(pair)
        i += 2
    return pairs

def encrypt_playfair(plaintext, key):
    key_square = generate_key_square(key)
    pairs = generate_pairs(plaintext)
    cipher_text = ""
    for pair in pairs:
        if len(pair) == 1:
            cipher_text += pair
            continue
        row1, col1 = divmod(key_square.index(pair[0]), 5)
        row2, col2 = divmod(key_square.index(pair[1]), 5)
        if row1 == row2:
            cipher_text += key_square[row1 * 5 + (col1 + 1) % 5]
            cipher_text += key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_square[((row1 + 1) % 5) * 5 + col1]
            cipher_text += key_square[((row2 + 1) % 5) * 5 + col2]
        else:
            cipher_text += key_square[row1 * 5 + col2]
            cipher_text += key_square[row2 * 5 + col1]
    return cipher_text

def decrypt_playfair(ciphertext, key):
    key_square = generate_key_square(key)
    pairs = generate_pairs(ciphertext)
    plaintext = ""
    for pair in pairs:
        if len(pair) == 1:
            plaintext += pair
            continue
        row1, col1 = divmod(key_square.index(pair[0]), 5)
        row2, col2 = divmod(key_square.index(pair[1]), 5)
        if row1 == row2:
            plaintext += key_square[row1 * 5 + (col1 - 1) % 5]
            plaintext += key_square[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[((row1 - 1) % 5) * 5 + col1]
            plaintext += key_square[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += key_square[row1 * 5 + col2]
            plaintext += key_square[row2 * 5 + col1]
    return plaintext

# Example usage:
plaintext = "Hello Gautam"
key = "HEll"
encrypted_text = encrypt_playfair(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt_playfair(encrypted_text, key)
print("Decrypted text:", decrypted_text)
