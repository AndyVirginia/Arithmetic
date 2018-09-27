import generator
import Stack
import infixTosuffix
from fractions import Fraction

class Calculator:
    def str_to_fraction(self, expression):
        suf = self.to_suffix_expression(expression)
        for x in range(len(suf)):
            if suf[x] not in self.list_operators:
                if suf[x].find('`') != -1:
                    a = suf[x].split('`')
                    inter = int(a[0])
                    b = a[1]
                else:
                    inter = 0
                    b = suf[x]
                if b.find('/') != -1:
                    c = b.split('/')
                    denominator = int(c[1])
                    numerator = int(c[0]) + inter * denominator
                else:
                    denominator = 1
                    numerator = inter
                new_num = Fraction(numerator, denominator)
                suf[x] = new_num
        return suf

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

