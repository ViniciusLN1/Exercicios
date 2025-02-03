from random import randint
computador = randint(1, 3)
print('-=-' * 17)
print('Tente adivinhar qual numero eu estou pensando!')
print('-=-' * 17)
jogador = int(input('Qual numero eu estou pensando?: '))
if jogador == computador:
    print('Voce ganhou!!!')
else:
    print('NT MONSTRO!!!!! O numero que eu estava pensando era {}'.format(computador))
