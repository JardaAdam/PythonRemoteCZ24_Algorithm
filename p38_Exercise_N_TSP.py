""" Problém obchodního cestujícího (TSP)
Dostali jste úkol naplánovat trasu obchodního cestujícího,
který musí navštívit všechna města v seznamu přesně jednou a poté se vrátit zpět do výchozího města.
Napište program, který najde nejkratší možnou trasu (minimální vzdálenost),
kterou může obchodní cestující absolvovat.
"""

from itertools import permutations


def count_distance(cities, path):
    distance = 0  # na začátku má trasa vzdálenost 0
    # následně procházím všechna města na trase a přičítám vzdálenost
    for i in range(len(path)-1):
        distance += cities[path[i]][path[i+1]]
    # z koncového města se zase musíme vrátit zpět do počátečního města
    distance += cities[path[-1]][path[0]]
    # vrátím výslednou vzdálenost
    return distance


def tsp(cities):
    n = len(cities)
    all_paths = permutations(range(n))
    minimal_distance = None
    best_path = None
    for path in all_paths:
        # spočítat vzdálenost aktuální trasy -> vytvořím si pomocnou funkci
        actual_distance = count_distance(cities, path)
        print(f"path={path}, distance={actual_distance}")
        # pokud je aktuální trasa kratší, než dříve nalezená minimal_distance, tak si ji uložím
        if not minimal_distance or minimal_distance > actual_distance:
            minimal_distance = actual_distance
            best_path = path
    # vrátím výslednou nejkratší trasu
    return best_path, minimal_distance


cities = [
   # A   B   C   D
    [0, 10, 15, 20],  # A
    [10, 0, 35, 25],  # B
    [15, 35, 0, 30],  # C
    [20, 25, 30, 0]   # D
    ]


best_path, minimal_distance = tsp(cities)
print(f"Minimal path: {best_path} with distance: {minimal_distance}.")
