morse_list = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '・－・－・－', ',': '－－・・－－', '?': '・・－－・・', "'": '．－－－－．',
    '!': '－・－・－－', '/': '－・・－・', '(': '－・－－・', ')': '－・－－・－',
    '&': '・－・・・', ':': '－－－・・・', ';': '－・－・－・', '=': '－・・・－',
    '+': '・－・－・', '-': '－・・・・－', '_': '・・－－・・－', '"': '・－・・－・',
    '$': '・・・・－・・－', '@': '・－－・－・'
}

morse_to_english = {value: key for key, value in morse_list.items()}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append('/')
        elif char in morse_list:
            morse_code.append(morse_list[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = []
    for code in morse_code:
        if code == '/':
            text.append(' ')
        elif code in morse_to_english:
            text.append(morse_to_english[code])
        else:
            text.append(code)
    return ''.join(text)

while True:
    choice = input("To convert English to Morse code, enter '1'\nTo convert Morse code to English, enter '2'\nTo exit, enter 'exit': ")
    
    if choice == '1':
        text = input("Enter the English text: ")
        morse_result = text_to_morse(text)
        print("Conversion result:", morse_result)
    elif choice == '2':
        morse_code = input("Enter the Morse code: ")
        text_result = morse_to_text(morse_code)
        print("Conversion result:", text_result)
    elif choice.lower() == 'exit':
        break
    else:
        print("Please enter a valid option.")
