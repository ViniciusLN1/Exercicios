import random
print('=======PEDRA PAPEL TESOURA=======')
print('''PEDRA - [1]
PAPEL - [2]
TESOURA - [3]''')
escolha = int(input('QUAL SUA ESCOLHA: '))
lista =[1, 2, 3]
escolhamaq = random.choice(lista)

if escolha == 1:
    print('Voce escolheu PEDRA!')
elif escolha == 2:
    print('Voce escolheu PAPEL!')
elif escolha == 3:
    print('Voce escolheu TESOURA!')

if escolhamaq == 1:
    print('A maquina escolheu PEDRA!')
elif escolhamaq == 2:
    print('A maquina escolheu PAPEL!')
elif escolhamaq == 3:
    print('A maquina escolheu TESOURA!')


if escolha == 1 and escolhamaq == 2:
    print('Voce perdeu!!!!')
elif escolha == 1 and escolhamaq == 3:
    print('Voce ganhou!!!!')
elif escolha == 2 and escolhamaq == 1:
    print('Voce ganhou!!!!')
elif escolha == 2 and escolhamaq == 3:
    print('Voce perdeu!!!')
elif escolha == 3 and escolhamaq == 1:
    print('Voce ganhou!!!')
elif escolha == 3 and escolhamaq == 2:
    print('Voce perdeu!!!')
else:
    print('EMPATE!!')
