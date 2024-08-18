"""Palindrom
Napište funkci, který zjistí, zda je daný řetězec palindrom.
Palindrom je řetězec, který se čte stejně zleva i zprava,
například 'madam' nebo 'racecar'.

is_palindrom("madam") -> True
is_palindrom("kobylamamalybok") -> True
is_palindrom("kokos") -> False
"""


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


if __name__ == '__main__':
    strings = ['Madam', 'kobylaMAmalyBOK', 'kokos']
    for string in strings:
        if is_palindrome(string):
            print(f"'{string}' je palindrom")
        else:
            print(f"'{string}' není palindrom")

    print(is_palindrome("MAdam"))
