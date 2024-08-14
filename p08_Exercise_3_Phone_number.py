"""Exercise 3: Phone number

Write a function that takes a list of 11 integers
and returns a string in a phone number format.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
## => returns "(+12) 345-678-901"###
"""

from typing import List


def create_phone_number(n: List[int]) -> str:
    return (f"(+{''.join(str(x) for x in n[0:2])}) "
            f"{''.join(str(x) for x in n[2:5])}-"
            f"{''.join(str(x) for x in n[5:8])}-"
            f"{''.join(str(x) for x in n[8:11])}")


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))
