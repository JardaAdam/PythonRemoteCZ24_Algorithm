"""Exercise 5: Morse code
Your Exercise is to implement a function that will accept a Morse-encoded expression as an input and return a decoded
string of human-understandable characters.
"""


MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str) -> str:
    # print(f"morse_code: '{morse_code}'")

    # Odstranit přebytečné mezery na začátku a konci morse_code # Extra spaces before or after the code have no meaning and should be ignored.
    morse_code = morse_code.strip()
    # print(f"morse_code.strip(): '{morse_code}'")

    # Rozsekám si zadání na jednotlivá slova
    morse_word_list = morse_code.split('   ')
    # print(f"morse_word_list: {morse_word_list}")
    result = ''
    for morse_word in morse_word_list:
        # Rozsekám si slova na jednotlivá písmena
        morse_char_list = morse_word.split()
        # print(f"morse_char_list: {morse_char_list}")

        # Každý znak převedu podle slovníku MORSE_CODE na písmeno
        for morse_char in morse_char_list:
            result += MORSE_CODE[morse_char]

        result += ' '

    # vrátím výsledek
    return result.strip()


if __name__ == "__main__":
    print(f"'{decode_morse('.... . -.--   .--- ..- -.. .')}'")  ## => 'HEY JUDE'
    print(f"'{decode_morse(' . ')}'")  ## => 'E'
    print(f"'{decode_morse('...   ---   ...')}'")  ## => 'S O S'
