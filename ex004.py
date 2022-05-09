from math import sin
from math import cos
from math import radians
from math import tan
ansen = float(input(' Digite o valor do angulo para calcular o seno '))
ancos = float(input(' Digite o valor do angulo para calcular o cos '))
atan = float(input(' Digite o valor do angulo para calcular a tangente '))
sen = sin(radians(ansen))
cos = cos(radians(ancos))
tan = tan(radians(atan))
print(' O valor do seno e {:.2f} '.format(sen))
print(' O valor do cos e {:.2f} '.format(cos))
print(' Vo calor da tangente e {:.2f}'.format(tan))
