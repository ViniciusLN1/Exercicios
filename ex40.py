nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Reprovado!')
elif media >= 5.0 and media < 7:
    print('Recuperação!')
elif media >= 7:
    print('Aprovado!')
