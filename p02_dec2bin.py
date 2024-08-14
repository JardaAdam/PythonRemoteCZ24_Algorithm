#d = int(input("Zadejte nezáporné celé číslo: "))

def dec2bin(d):
    binary = ""

    while True:
        r = d % 2

        if r == 1:
            binary = '1' + binary
        else:
            binary = '0' + binary

        d = d // 2

        if d == 0:
            return(binary)


if __name__ == '__main__':
    for i in range(1, 21):
        print(f"{i}: {dec2bin(i)}")
