"""Exercise 4: Weird string

Write the function WeIrD CaSe, which accepts a string
and returns it with all even numbers as characters, all uppercase,
and odd letters lowercase. Use indexing from zero.
"""


def to_weird_case(string: str) -> str:
    words = string.split()
    result = ''
    for word in words:
        for index, character in enumerate(word):
            if index % 2:
                result += character.lower()
            else:
                result += character.upper()
        result += ' '
    return result.strip()


if __name__ == "__main__":
    strings = ['String', 'Weird string', 'Algorithms and data structures']
    for one_string in strings:
        print(f"{one_string} -> '{to_weird_case(one_string)}'")
