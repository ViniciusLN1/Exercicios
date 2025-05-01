soma_idade = 0
media_idade = 0
maioridadehomem = 0
nome_velho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------ {p} pessoa ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    soma_idade = soma_idade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
media_idade = soma_idade / 4
print(f'A media de idade do grupo e de {media_idade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nome_velho}.')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos.')