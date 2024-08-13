#a = int(input("Input first number: "))
#b = int(input("Input second number: "))

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == "__main__":
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    print(f"gcd({a}, {b}) = {gcd(a, b)}")
