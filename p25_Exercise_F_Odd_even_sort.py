"""
Uspořádáme seznam celých čísel tak,
že nejprve budou všechna lichá čísla (uspořádaná podle velikosti)
a následně všechna sudá čísla (uspořádaná podle velikosti).
[5, 3, 4, 2, -6, 7, -7, 8, 1, 2] -> [-7, 1, 3, 5, 7, -6, 2, 2, 4, 8]
"""
from p23_quicksort import quicksort


def odd_even_quicksort(arr):
    return quicksort([x for x in arr if x % 2]) + quicksort([x for x in arr if x % 2 == 0])


if __name__ == '__main__':
    unsorted = [5, 3, 4, 2, -6, 7, -7, 8, 1, 2]
    print(odd_even_quicksort(unsorted))
