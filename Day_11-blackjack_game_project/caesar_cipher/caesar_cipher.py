from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again = True

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    cipher_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            index += shift
            if index > 25:
                index %= 26
            cipher_text += alphabet[index]
        else:
            cipher_text += char
    print(f"The {direction}d text is", cipher_text)

while(go_again):
    en_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    msg = input("Type your message:\n").lower()
    shift_value = int(input("Type the shift number:\n"))
    caesar(msg, shift_value, en_direction)
    msg = input("Do you wish to go again, Yes or No ? ")
    if msg.lower() == "no":
        go_again = False
