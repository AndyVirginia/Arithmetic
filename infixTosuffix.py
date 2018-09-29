import Stack
from fractions import Fraction


class infix_to_suffix:
    def __init__(self):
        self.list_operators = ["+", "-", "×", "÷", "(", ")", "="]
        self.pri_operators = {"+": 0, "-": 0, "×": 1, "÷": 1}

    def to_suffix_expression(self, expression):
        '''生成逆波兰表达式'''
        stack_operator = Stack.Stack()
        suffix_expression = []
        list_temp = []
        expression = expression + "="
        for element in expression:
            if element not in self.list_operators:
                list_temp.append(element)
            elif element == "=":
                if len(list_temp) != 0:
                    str_temp = ""
                    for i in range(0, len(list_temp)):
                        str_temp = str_temp+list_temp.pop(0)
                    suffix_expression.append(str_temp)
            else:
                if len(list_temp) != 0:
                    str_temp = ""
                    for i in range(0, len(list_temp)):
                        str_temp = str_temp+list_temp.pop(0)
                    suffix_expression.append(str_temp)
                if stack_operator.isEmpty() or element == "(":
                    stack_operator.push(element)
                elif element != "(" and element != ")":
                    if stack_operator.peek() != "(" and self.pri_operators[element] > self.pri_operators[
                        stack_operator.peek()]:
                        stack_operator.push(element)
                    else:
                        while True:
                            if stack_operator.peek() == "(":
                                stack_operator.push(element)
                                break
                            elif self.pri_operators[element] < self.pri_operators[stack_operator.peek()]:
                                while not stack_operator.isEmpty() and True:
                                    str_operator = stack_operator.peek()
                                    if str_operator == "(" or self.pri_operators[str_operator] < self.pri_operators[
                                        element]:
                                        break
                                    else:
                                        stack_operator.pop()
                                        suffix_expression.append(str_operator)
                            else:
                                suffix_expression.append(stack_operator.pop())
                            if stack_operator.isEmpty():
                                stack_operator.push(element)
                                break
                elif element == ")":
                    while True:
                        if stack_operator.peek() != "(":
                            suffix_expression.append(stack_operator.pop())
                        else:
                            stack_operator.pop()
                            break
                else:
                    stack_operator.push(element)
        if not stack_operator.isEmpty():
            while not stack_operator.isEmpty():
                suffix_expression.append(stack_operator.pop())
        return suffix_expression

    def str_to_fraction(self, suf):
        '''字符串转换为fraction类'''
        for x in range(len(suf)):
            if suf[x] not in self.list_operators:
                y = suf[x].strip()
                if y.find('`') == -1:
                    if y.find('/') == -1:
                        numerator =  int(y)
                        denominator = 1
                    else:
                        a = y.split('/')
                        numerator = int(a[0])
                        denominator = int(a[1])
                else:
                    a = y.split('`')
                    inter = int(a[0])
                    b = a[1].split('/')
                    denominator = int(b[1])
                    numerator = int(b[0]) + inter * denominator
                new_num = Fraction(numerator,denominator)
                suf[x] = new_num
        return suf
