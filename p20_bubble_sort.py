from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)-1):
        #print(arr)
        changed = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changed = True
        if not changed:
            return arr
    return arr


if __name__ == '__main__':
    my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    #my_numbers = [1, 2, 2, 2, 3, 4, 4, 5, 7, 8, 9, 14]
    print(bubble_sort(my_numbers))
