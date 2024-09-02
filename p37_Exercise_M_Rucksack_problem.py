"""
Máte batoh s určitou kapacitou a řadu předmětů,
z nichž každý má určitou váhu a hodnotu.
Napište program, který vybere předměty tak, aby maximalizoval celkovou hodnotu,
aniž by překročil kapacitu batohu.
"""


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


items = [Item(10, 60),
         Item(20, 100),
         Item(30, 120),
         Item(15, 70),
         Item(8, 45)]

capacity = 50


def sack(capacity, items):
    n = len(items)
    solutions = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]

    for i in range(1, n+1):  # pro každý prvek (item)
        print(i, end=': ')
        for w in range(1, capacity+1):  # pro každou váhu (weight)
            if items[i-1].weight <= w:
                solutions[i][w] = max(solutions[i-1][w], solutions[i-1][w-items[i-1].weight] + items[i-1].value)
            else:
                solutions[i][w] = solutions[i-1][w]
            print(solutions[i][w], end=' ')
        print()
    return solutions[n][capacity]


print(f"Maximální hodnota předmětů v batohu je {sack(capacity, items)}.")
