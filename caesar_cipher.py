alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(direction, received_text, shift_num):
    encrypted_text = ''

    if direction == 'decode':
        shift_num *= -1

    for char in received_text:
        try:
            encrypted_text += alphabet[alphabet.index(char) + shift_num]
        except IndexError:
            encrypted_text += alphabet[(alphabet.index(char) + shift_num - len(alphabet))]


    print(encrypted_text)

caesar_cipher(direction, text, shift)
