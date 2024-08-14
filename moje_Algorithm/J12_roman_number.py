"""Převod římských číslic na arabské
Napište funkci, která převede římské číslo na arabské (běžné celé číslo).
Římské číslice jsou I, V, X, L, C, D, M a mají hodnoty 1, 5, 10, 50, 100, 500, 1000.

Tip:
Při převodu je třeba mít na paměti, že pokud menší číslice předchází větší,
hodnota menší číslice se odečítá (např. IV = 4, IX = 9).

rom2dec('MMXXIV') -> 2024
"""
rom_numbers = \
    {'I' : 1,
     'V' : 5,
     'X' : 10,
     'L' : 50,
     'C' : 100,
     'D' : 500,
     'M' : 1000}
def rom2dec(romstr: str):
    result = 0
    for i in range(len(romstr)):
        result += rom_numbers[romstr[i]]
        if i < len(romstr) - 1:
            if rom_numbers[romstr[i]] < rom_numbers[romstr[i + 1]]:
                result -= 2 * rom_numbers[romstr[i]]
    return result


print(f"'{rom2dec('MMXXIV')}'")
print(rom2dec('MMXLI'))