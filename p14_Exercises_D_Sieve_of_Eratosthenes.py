"""Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Napište program, který vygeneruje všechna prvočísla menší než N
pomocí algoritmu Eratosthenovo síto.

Eratosthenovo síto funguje tak, že postupně "odškrtáváte" násobky každého čísla počínaje 2,
které jsou tím pádem složená čísla. Čísla, která zůstanou neodškrtnutá, jsou prvočísla.
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# vypsat všechna prvočísla menší než n (10000)
def print_n_prime_numbers(n: int):
    for i in range(n+1):
        if is_prime(i):
            print(i, end=" ")
    print()


"""
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
F  F  T  T  F  T  F  T  F  F   F   T   F   T   F   F   F   T   F   T   F
"""
def sieve_of_eratosthenes(n):
    # vygenerujeme seznam sieve velikosti n+1 (True)
    sieve = [True] * (n+1)

    # sieve[0] a sieve[1] = False
    sieve[0] = sieve[1] = False

    # posouvám se v seznamu, každé číslo, které je True, je prvočíslo -> vypíšu
    for i in range(2, (n+1)//2):
        if sieve[i]:
            for j in range(i*2, n+1, i):
                # první číslo v seznamu, které je True, je prvočíslo, smažu všechny jeho násobky ze seznamu (False)
                sieve[j] = False

    # vypíšu indexy, na kterých je True
    for i in range(n+1):
        if sieve[i]:
            print(i, end=" ")
    print()


if __name__ == '__main__':
    n = 10000
    print_n_prime_numbers(n)
    sieve_of_eratosthenes(n)
