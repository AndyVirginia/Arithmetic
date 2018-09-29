from generator import Ari_Expression
from infixTosuffix import infix_to_suffix
import Calculate
from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-n", action="store", type="int", dest="problem",default='10', help='题目个数')
    parser.add_option("-r", action="store", type='int', dest="max_num", default="10", help="题目操作数取值范围",)
    i = 1
    (options, args) = parser.parse_args()
    correct = []
    wrong = [] 
    p = open('Exercises.txt', 'w')
    r = open('Answer.txt', 'w')
    while i < options.problem + 1:
        ari = Ari_Expression(options.max_num)
        inf = infix_to_suffix()
        try:
            real_res = Calculate.getResult(inf.str_to_fraction(inf.to_suffix_expression(ari.str)))
        except ValueError:
            continue
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
    print('题目正确率：' + str(100 * len(correct)/options.problem)+'%')
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
