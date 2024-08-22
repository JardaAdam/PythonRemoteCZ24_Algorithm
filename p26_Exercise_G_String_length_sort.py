"""
Uspořádáme texty v seznamu podle délky:
["Ahoj", "Hello", "Hi", "Nazdar", "Čau"] -> ["Hi", "Čau", "Ahoj", "Hello", "Nazdar"]

BONUS: Pokud mají slova stejnou délku, řadíme abecedně.
"""


def string_length_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    len_pivot = len(arr[0])
    middle = ([x for x in arr if len(x) == len_pivot and x < pivot] +
              [x for x in arr if len(x) == len_pivot and x == pivot] +
              [x for x in arr if len(x) == len_pivot and x > pivot])
    left = [x for x in arr if len(x) < len_pivot]
    right = [x for x in arr if len(x) > len_pivot]
    return string_length_quicksort(left) + middle + string_length_quicksort(right)


if __name__ == '__main__':
    strings = ["Pápá", "Ahoj", "Hello", "Hi", "Nazdar", "Čau"]
    print(string_length_quicksort(strings))
