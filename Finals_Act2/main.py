from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from PositionalList import PositionalList as PositionalList

def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
def infixToPostfix(s):
    S=Stack
    S = []
    result = ""

    for i in range(len(s)):
        c = s[i]
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            result += c
        elif c == '(':
            S.append('(')
        elif c == ')':
            while S and S[-1] != '(':
                result += S.pop()
            S.pop()
        else:
            while S and (prec(c) <= prec(S[-1])):
                result += S.pop()
            S.append(c)
    while S:
        result += S.pop()
    return result

exp = input("Enter an infix expression: ")
postfix = infixToPostfix(exp)
print("Postfix notation:", postfix)