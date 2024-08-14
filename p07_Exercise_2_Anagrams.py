"""Exercise 2: Anagrams
Write a function that finds all the anagrams of a given word
from the list provided. Words found should be return as a list.

"""
from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    result = []
    sorted_word = sorted(word)
    for second_word in lst_of_words:
        if sorted_word == sorted(second_word):
            result.append(second_word)
    return result


if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
