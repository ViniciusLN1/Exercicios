#Jeito mais longo!
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior valor digitado eh o {}'.format(numero1))
if numero2 > numero1 and numero2 > numero3:
    print('O maior valor digitado eh o {}'.format(numero2))
if numero3 > numero1 and numero3 > numero2:
    print('O maior valor digitado eh o {}'.format(numero3))

if numero1 < numero2 and numero1 < numero3:
    print('O menor valor digitado eh o {}'.format(numero1))
if numero2 < numero1 and numero2 < numero3:
    print('O menor valor digitado eh o {}'.format(numero2))
if numero3 < numero1 and numero3 < numero2:
    print('O menor valor digitado eh o {}'.format(numero3))

#Jeito mais curto
