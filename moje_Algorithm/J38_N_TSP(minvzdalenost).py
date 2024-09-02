""" Problém obchodního cestujícího (TSP)
Dostali jste úkol naplánovat trasu obchodního cestujícího,
který musí navštívit všechna města v seznamu přesně jednou a poté se vrátit zpět do výchozího města.
Napište program, který najde nejkratší možnou trasu (minimální vzdálenost),
kterou může obchodní cestující absolvovat.
"""

from itertools import permutations


def count_distance(cities, path):
    distance = 0 # pocatecni vzdalenost
    # nasledne prochazim vsechna mesta a pocitam vzdalenost
    for i in range(len(path)-1):
        distance += cities[path[i]][path[i + 1]]

    # pridani vzdalenosti zpet do vychoziho mesta
    distance += cities[path[-1]][path[0]]
    return distance

def tsp(cities):
    n = len(cities)
    all_paths = permutations(range(n))

    minimal_distance = float('int') #inicializace s nekonecnem
    best_path = None

    for path in all_paths:
    #    print(f"path={path}, distance={actual_distance}")
        distance = count_distance(cities, path)
        if distance < minimal_distance:
            minimal_distance = distance
            best_path = path

    return best_path, minimal_distance


cities = [
   # A   B   C   D
    [0, 10, 15, 20],  # A
    [10, 0, 35, 25],  # B
    [15, 35, 0, 30],  # C
    [20, 25, 30, 0]   # D
    ]

best_path, minimal_distance = tsp(cities)
print(f"Nejkratší trasa je: {best_path} s minimální vzdáleností: {minimal_distance}")