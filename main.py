from generator import Ari_Expression
from infixTosuffix import infix_to_suffix
import Calculate


def main():
    max_num = int(input('请输入操作数的最大值：'))
    problem = int(input('请输入需要的题目数量：'))
    i = 1
    correct = []
    wrong = [] 
    p = open('Exercises.txt', 'w')
    r = open('Answer.txt', 'w')
    while i < problem + 1:
        ari = Ari_Expression(max_num)
        inf = infix_to_suffix()
        real_res = Calculate.getResult(inf.str_to_fraction(inf.to_suffix_expression(ari.str)))
        if real_res >= 0:
            real_res = ari.str_num(real_res)
            print(str(i)+'. ' + ari.str, end = '')
            p.write(str(i)+'. ' + ari.str + '\n')
            r.write(str(i)+'. ' + real_res + '\n')
            res = input()
            if res == real_res:
                correct.append(i)
            else:
                wrong.append(i)
            i += 1
    p.close()
    r.close()
    print('题目正确率：' + str(len(correct)/problem))
    g = open('Grade.txt','w')
    g.write('Correct:' + str(len(correct))+'(')
    for x in correct:
        g.write(str(x)+', ')
    g.write(')\n')
    g.write('Wrong:' + str(len(wrong))+'(')
    for x in wrong:
        g.write(str(x)+', ')
    g.write(')\n')


if __name__ == '__main__':
    main()
