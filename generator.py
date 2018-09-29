from fractions import Fraction
import random


class Ari_Expression():
    '''算术表达式的生成'''
    def __init__(self, max_num):
        self.init_operators()
        self.init_nums(max_num)
        self.init_expression()

    def init_num(self, max_num):
        '''随机生成数'''
        denominator = random.randint(1, max_num)
        numerator = random.randint(0, max_num)
        return Fraction(numerator, denominator)

    def insert_bracket(self):
        '''插入括号'''
        bracket = ['(', 'null', ')']
        if len(self.operators) > 1:
            x = random.randint(0, len(self.operators))
            while x < len(self.operators):
                y = random.randint(x, len(self.operators))
                low = False
                for a in self.operators[x:y+1]:
                     if a in ['+', '-']:
                         low = True
                         break
                try:
                    if self.operators[y+1] in ['×', '÷'] and low:
                        self.operators.insert(x, '(')
                        self.operators.insert(y+2,')')
                except IndexError:
                    pass
                x = y+2
            

    def init_operators(self):
        '''随机生成一个运算符并随机插入括号'''
        self.operators = []
        operator = ['+', '-', '×', '÷', 'null']
        for x in range(3):
            if x == 1:
                self.operators.append(random.choice(operator[:-2]))
            else:
                y = random.choice(operator)
                if y != 'null':
                    self.operators.append(y)
        self.insert_bracket()
    
    def init_nums(self, max_num):
        self.nums = []
        self.nums.append(self.init_num(max_num))
        for x in range(len(self.operators)):
            y = self.init_num(max_num)
            if self.operators[x] == '÷':
                while y.numerator == 0:
                    y = self.init_num(max_num)
            self.nums.append(y)
    
    def str_num(self, num):
        '''字符串化一个分数'''
        inter = int(num.numerator / num.denominator)
        numerator = int(num.numerator % num.denominator)
        str_num = ''
        if numerator != 0:
            str_num += str(numerator) + '/' + str(num.denominator)
        if not str_num:
            '''如果为空'''
            str_num += str(inter)
        else:
            if inter == 0:
                return str_num
            else:
                str_num = str(inter) + '`' + str_num
        return str_num
    
    def init_expression(self):
        '''生成一个算术表达式的字符串形式'''
        self.str = ''
        i = 0
        self.exp = []
        again = False
        for x in self.operators:
            if again:
                self.str += x + ' '
            elif x == '(':
                self.str += x + ' '
            elif x == ')':
                self.str += self.str_num(self.nums[i]) + ' '
                i += 1
                self.str += x + ' '
                again = True
            else:
                self.str += self.str_num(self.nums[i]) + ' '
                self.str += x + ' '
                i += 1
        self.str += self.str_num(self.nums[-1]) + ' ='
