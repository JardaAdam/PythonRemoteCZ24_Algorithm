"""Vyhledání nejdelšího společného prefixu
Napište funkci, která najde nejdelší společný prefix (počáteční část) všech řetězců v seznamu.
Pokud žádný společný prefix neexistuje, funkce by měla vrátit prázdný řetězec.

longest_prefix(['abba', 'abeceda', 'ababa']) -> 'ab'
longest_prefix(['abba', 'abeceda', 'tata']) -> ''
"""


def longest_prefix(words):
    if len(words) == 0:
        return ''
    if len(words) == 1:
        return words[0]
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            # print(f"prefix : '{prefix}'")
            prefix = prefix[:-1]
    return prefix


if __name__ == "__main__":
    print(f"'{longest_prefix(['abba', 'abeceda', 'ababa'])}'")
    print(f"'{longest_prefix(['abba', 'abeceda', 'tata'])}'")
    print(f"'{longest_prefix(["květina", "květ", "květen"])}'")
