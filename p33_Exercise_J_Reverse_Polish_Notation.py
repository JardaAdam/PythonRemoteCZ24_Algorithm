"""Vyhodnocení výrazu v postfixové notaci (Reverse Polish Notation - RPN)

Zadání:
Napište funkci, která vyhodnotí aritmetický výraz zadaný v postfixové notaci.

Například:
"1 2 +" -> 3
"8 2 /" -> 4
"5 1 2 + 4 * + 3 -" ->
"5 3 4 * + 3 -" ->
"5 12 + 3 -" ->
"17 3 -" ->
"14" -> 14.
"
"""


def rpn(s: str) -> int:
    stack = []
    for token in s.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 / num2)
    return stack.pop()


if __name__ == '__main__':
    strings = ["1 2 +", "8 2 /", "5 1 2 + 4 * + 3 -"]
    for string in strings:
        print(f"'{string}' -> {rpn(string)}")
