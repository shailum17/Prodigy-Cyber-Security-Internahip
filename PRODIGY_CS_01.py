letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

# Function for encryption of the plain text 

def encryption (plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext = ciphertext + letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index = new_index - num_letters
                ciphertext += letters[new_index]
        return ciphertext

# Function for decryption of the cipher text 
    
def decryption (ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext = plaintext + letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index = new_index + num_letters
                plaintext += letters[new_index]
        return plaintext



print()
print('CEASAR CIPHER PROGRAM')
print()
print('Do you want to encrypt or decrypt')
user_input = input('e/d: ').lower()
print()

if user_input =='e':
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key size (In between 1 to 26): '))
    text = input('Enter the text that user wants to encrypt : ')
    ciphertext = encryption(text, key)
    print(f'CIPHERTEXT: {ciphertext} ')

elif user_input =='d':
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key size (In between 1 to 26): '))
    text = input('Enter the text that user wants to Decrypt : ')
    plaintext = decryption(text, key)
    print(f'PLAINTEXT: {plaintext} ')
