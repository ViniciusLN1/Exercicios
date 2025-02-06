numero = int(input('Digite um numero! '))
base = int(input('''Qual vai ser a base da conversão?)
(1) - Binario
(2) - Octal
(3) - Hexadecimal
'''))
if base == 1:
    print('O seu número em BINARIO é {}'.format(bin(numero)[2:]))
elif base == 2:
    print('O seu número em OCTAL é {}'.format(oct(numero)[2:]))
elif base == 3:
    print('O seu número em HEXADECIMAL é {}'.format(hex(numero) [2:]))
else:
    print('ERRO! Tente novamente!')
