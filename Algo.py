import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# ceaser cipher algorithm
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + (shift%26)  # shift only alphabets
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text




import random
import string

def generate_monoalphabetic_key():
    # Generating a random mapping of letters for the cipher
    letters = list(string.ascii_lowercase)
    shuffled_letters = letters[:]
    random.shuffle(shuffled_letters)
    return ''.join(shuffled_letters)

def monoalphabetic_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += key[ord(char) - ord('a')]
            elif char.isupper():
                encrypted_text += key[ord(char.lower()) - ord('a')].upper()
        else:
            encrypted_text += char
    return encrypted_text

def monoalphabetic_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(key.index(char) + ord('a'))
            elif char.isupper():
                decrypted_text += chr(key.index(char.lower()) + ord('a')).upper()
        else:
            decrypted_text += char
    return decrypted_text


# polyalphabetic cipher algorithm
def generate_vigenere_key(keyword, text_length):
    keyword = keyword.lower()
    key = ''
    index = 0
    for i in range(text_length):
        if index == len(keyword):
            index = 0
        key += keyword[index]
        index += 1
    return key

def polyalphabetic_encrypt(plaintext, keyword):
    alphabet = string.ascii_lowercase
    encrypted_text = ''
    keyword = generate_vigenere_key(keyword, len(plaintext))


    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(keyword[i]) - ord('a')
            if char.islower():
                encrypted_text += alphabet[(alphabet.index(char) + shift) % 26]
            else:
                encrypted_text += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
        else:
            encrypted_text += char

    return encrypted_text

def polyalphabetic_decrypt(ciphertext, keyword):
    alphabet = string.ascii_lowercase
    decrypted_text = ''
    keyword = generate_vigenere_key(keyword, len(ciphertext))

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(keyword[i]) - ord('a')
            if char.islower():
                decrypted_text += alphabet[(alphabet.index(char) - shift) % 26]
            else:
                decrypted_text += alphabet[(alphabet.index(char.lower()) - shift) % 26].upper()
        else:
            decrypted_text += char

    return decrypted_text


# playfair cipher algorithm

def generate_playfair_matrix(key):
    key = key.replace('J', 'I')
    key = ''.join(dict.fromkeys(key))  # Remove duplicates while preserving order
    alphabet = string.ascii_uppercase.replace('J', '')
    key += ''.join(filter(lambda x: x not in key, alphabet))
    matrix = [key[i:i + 5] for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)

def playfair_encrypt(plaintext, key):
    plaintext.replace(" ","")
    for i,l in enumerate(plaintext):
        if(i!= 0):
            if(l == plaintext[i-1] and i%2 != 0):
                plaintext = plaintext[:i] + 'X' + plaintext[i:]
        
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    matrix = generate_playfair_matrix(key)
    ciphertext = ""
    
    for pair in plaintext:
        if len(pair) == 1:
            pair += 'X'
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    ciphertext.replace(" ","")
    matrix = generate_playfair_matrix(key)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, letter1)
        row2, col2 = find_position(matrix, letter2)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext


# Image Encryption
def encrypt_image(image_path, key):
    # Open the image file
    with open(image_path, 'rb') as f:
        data = f.read()

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)

    # Encrypt the data
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))

    return ct_bytes, cipher.iv

    # Save the encrypted data to a file
    # with open('encrypted_image.enc', 'wb') as f:
    #     f.write(cipher.iv)
    #     f.write(ct_bytes)

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image file
    with open(encrypted_image_path, 'rb') as f:
        iv = f.read(16)
        ct = f.read()

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Decrypt the data
    pt = unpad(cipher.decrypt(ct), AES.block_size)


    return pt

    # Save the decrypted data to a file
    # with open('decrypted_image2.jpg', 'wb') as f:
    #     f.write(pt)

def generate_aes_key():
    return get_random_bytes(16)

    










