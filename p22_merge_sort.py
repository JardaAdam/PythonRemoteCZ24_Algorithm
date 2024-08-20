from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    #print(arr)
    if len(arr) > 1:
        # rozdělíme pole na dvě části (skoro poloviny)
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # na každé toto menší pole aplikujeme merge_sort (rekurze)
        merge_sort(left)
        merge_sort(right)

        # sloučení obou částí do jednoho (seřazeného) seznamu
        left_index = right_index = merged_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                arr[merged_index] = left[left_index]
                left_index += 1
            else:
                arr[merged_index] = right[right_index]
                right_index += 1
            merged_index += 1

        # přidáme zbývající hodnoty z levého seznamu
        while left_index < len(left):
            arr[merged_index] = left[left_index]
            left_index += 1
            merged_index += 1

        # přidáme zbývající hodnoty z pravého seznamu
        while right_index < len(right):
            arr[merged_index] = right[right_index]
            right_index += 1
            merged_index += 1


if __name__ == '__main__':
    numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    merge_sort(numbers)
    print(numbers)
