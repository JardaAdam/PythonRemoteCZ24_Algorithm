"""Počet ostrovů
Máte dvourozměrné pole, kde 1 představuje zemi a 0 představuje vodu.
Napište funkci, která spočítá počet ostrovů.
Ostrov je souvislá oblast země, která je obklopena vodou a tvoří ji buňky, které sousedí vodorovně nebo svisle."""


def number_of_islands(grid):
    pass


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

print(f"Number if islands: {number_of_islands(grid)}")
