distancia = float(input('Qual a distancia da sua viajem? :'))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O preco da sua passagem vai ser de R${:.2f}'.format(passagem))
