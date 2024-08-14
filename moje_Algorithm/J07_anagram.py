from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    sorted_word = (sorted(word))
    return [w for w in lst_of_words if sorted(w) == sorted_word]
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))# => ['aabb', 'bbaa']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))# => ['carer', 'racer']

print(anagrams('laser', ['lazing', 'lazy', 'lacer']))# => []