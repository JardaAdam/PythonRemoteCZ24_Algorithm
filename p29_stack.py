""" Závorky
Napište funkci, která má jako parametr string obsahující závorky.
Funkce vrátí True, pokud jsou závorky "správně", jinak False

()
(())
)( -> ()
(()
(()))(
(()))((())
1210-
((()())())
1232321210
"""


def brackets(word):
    count = 0
    for c in word:
        #print(c)
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


"""
([)] -> False
([]) -> True
([][{}]) -> True

({[]<[]>}()) -> True
Zásobník: []

({[][<]>}()) -> False
Zásobník: ['(', '{', '[', '<'] - False
"""
def brackets2(word):
    stack = []
    for c in word:
        if c in "([{<":
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif c == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif c == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif c == '>':
            if len(stack) == 0 or stack.pop() != '<':
                return False
        #print(stack)
    return True


if __name__ == '__main__':
    words = ["()", "(())", "(()", ")(", "(()))((())", "((()())())"]
    for w in words:
        print(f"{w} -> {brackets(w)} -> {brackets2(w)}")

    words = ["([)]", "([])", "([][{}])", "({[]<[]>}())", "({[][<]>}())", ")}", "([)]"]
    for w in words:
        print(f"{w} -> {brackets2(w)}")
