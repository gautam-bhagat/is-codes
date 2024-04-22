def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value for encryption: "))

    encrypted_text = caesar_encrypt(plaintext, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print("\nOriginal Text:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
