"""Vyhledání nejdelšího společného prefixu
Napište funkci, která najde nejdelší společný prefix (počáteční část) všech řetězců v seznamu.
Pokud žádný společný prefix neexistuje, funkce by měla vrátit prázdný řetězec.

longest_prefix(['abba', 'abeceda', 'ababa']) -> 'ab'
longest_prefix(['abba', 'abeceda', 'tata']) -> ''
"""

def longest_prefix(strs: list) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):  # startswitch
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    print(f"'{longest_prefix(['abba', 'abeceda', 'ababa'])}'") # -> 'ab'
    print(f"'{longest_prefix(['abba', 'abeceda', 'tata'])}'") # -> ''