"""Palindrom
Napište funkci, který zjistí, zda je daný řetězec palindrom.
Palindrom je řetězec, který se čte stejně zleva i zprava,
například 'madam' nebo 'racecar'.

is_palindrom("madam") -> True
is_palindrom("kobylamamalybok") -> True
is_palindrom("kokos") -> False
"""


def is_palindrom(string):
    string = string.lower()
    return string == string[::-1]


if __name__ == '__main__':
    strings = ['Madam', 'kobylaMAmalyBOK', 'kokos']
    for string in strings:
        if is_palindrom(string):
            print(f"'{string}' je palindrom")
        else:
            print(f"'{string}' není palindrom")
