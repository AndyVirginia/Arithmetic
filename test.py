from generator import Ari_Expression
from infixTosuffix import infix_to_suffix
import Calculate


ari = Ari_Expression(10)
print(ari.str)
inf = infix_to_suffix()
x = inf.to_suffix_expression(ari.str)
print(x)
y = inf.str_to_fraction(x)
print(y)
print(Calculate.getResult(y))

