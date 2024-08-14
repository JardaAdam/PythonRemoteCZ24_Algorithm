"""
Nejmenší společný násobek (zkratka NSN či n, anglicky least common multiple – LCM)
několika daných čísel je nejmenší kladné celé číslo,
které je celočíselným násobkem všech daných čísel.
"""


def lcm(a, b):
    n = a
    while n % b:
        n += a
    return n


a = int(input("Zadej číslo a: "))
b = int(input("Zadej číslo b: "))
print(f"lcm({a}, {b}) = {lcm(a, b)}")
