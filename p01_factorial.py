n = int(input("Enter positive number: "))

i = 1
s = 1

while i <= n:
    s = s * i
    i = i + 1

print(f"{n}! = {s}")
