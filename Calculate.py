from fractions import Fraction

import generator
import infixTosuffix
import Stack

def getResult(expression):
    stackValue = []
    for item in expression:
        if item in ["+", "-", "×", "÷"]:
            n2 = stackValue.pop()
            n1 = stackValue.pop()
            result = cal(n1, n2, item)
            stackValue.append(result)
        else:
            stackValue.append(item)
    return stackValue[0]

def cal(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "×":
        return n1 * n2
    if op == "÷":
        return n1 / n2
