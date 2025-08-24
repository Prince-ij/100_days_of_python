# THIS PROGRAM TAKES ANY STRING AND OUTPUT THE MORSE CODE EQUIVALENT.

alphabet_morse_dict = {
    'A': '.-',
    'B': '-..',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

punctuations = ',./!@#$%^&*():\'" '
def to_morse(str):
    morse_string = []
    for char in str:
        if char in punctuations:
            morse_string.append(f'{char}')
        elif alphabet_morse_dict[char.upper()]:
            morse_string.append(f'{alphabet_morse_dict[char.upper()]}')
        else:
            morse_string.append(f'{char}')

    morse_string = ''.join(morse_string)
    return morse_string


def main():
    print('.................TEXT TO MORSE CODE CONVERTER.................')
    text = input('Transform your text to morse code: ')
    print('The Morse Code Equivalent is : 👇')
    print(to_morse(text))
main()
