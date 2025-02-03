import math
angulo = int(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O seno do angulo eh {:.2f}'.format(seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno do angulo eh {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do angulo eh {:.2f}'.format(tangente))
