"""
factors(5) -> [5]
factors(8) -> [2, 2, 2]
factors(10) -> [2, 5]
"""


def factors(n):
    divider = 2
    result = []
    while n > 1:
        while n % divider == 0:
            result.append(divider)
            n //= divider
        divider += 1
    return result


if __name__ == '__main__':
    for i in range(2, 21):
        print(f"factors({i}) = {factors(i)}")

