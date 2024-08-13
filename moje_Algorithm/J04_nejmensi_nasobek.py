def nsn(a, b):
    i = max(a, b)
    while True:
        print(i)
        if i % a == 0 and i % b == 0:
            return i
        i += max(a, b)

print(nsn(5, 12))