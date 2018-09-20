import random
import math


class Operator():
    '''随机生成一个算数运算符的列表'''
    def __init__(self):
        operator = ['+', '-', '×', '÷', 'null']
        self.str = []
        for x in range(3):
            if x == 1:
                self.str.append(random.choice(operator[:-2]))
            else:
                x = random.choice(operator)
                if x != 'null':
                    self.str.append(x)


class Num():
    '''生成随机数'''
    def creat_num(self, max_num):
        # 假分数时的分子,做乘除法运算有用
        self.full_numerator = random.randint(0, self.denominator * max_num)   
        # 带分数的整数部分
        self.inter = math.floor(self.full_numerator / self.denominator) 
        # 带分数的分子
        self.numerator = self.full_numerator % self.denominator      

    def __init__(self, max_num):
        '''初始化方法'''
        self.denominator = random.randint(1, max_num)    # 分母
        self.creat_num(max_num)
        self.output_str()

    def output_str(self):
        '''创建随机数的字符串形式'''
        if self.numerator == 0:
            # 分子等于0时
            if self.inter == 0:
                self.str = '0'
            else:
                self.str = str(self.inter)
        elif self.inter == 0:
            self.str = str(self.numerator) +'/'+ str(self.denominator)
        else:
            self.str = str(self.inter) +'\''+ str(self.numerator) +'/'+ str(self.denominator)
    
    def zero(self):
        '''判零函数'''
        if self.full_numerator == 0 and self.inter == 0:
            return True
        else:
            return False


class AriExpression():
    ''' 算术表达式的生成 '''
    def create_nums(self, max_num):
        '''创建运算数的列表'''
        self.nums = []
        self.nums.append(Num(max_num))
        for x in range(len(self.operator.str)):
            new_num = Num(max_num)
            if self.operator.str[x] == '÷':
                while new_num.zero():
                    new_num = Num(max_num)
            self.nums.append(new_num)
    
    def create_expression(self):
        '''创建表达式的字符串表示'''
        self.exp = ''
        for x in range(len(self.operator.str)):
            self.exp += self.nums[x].str + ' '
            self.exp += self.operator.str[x] + ' '
        self.exp += self.nums[-1].str + ' ='

    def __init__(self, max_num):
        self.operator = Operator()
        self.create_nums(max_num)
        self.create_expression()


for x in range(100):
    ari = AriExpression(10)
    print(ari.exp)
