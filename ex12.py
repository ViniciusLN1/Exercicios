preco = float(input('Qual o preco do produto? R$'))
desconto = preco*5/100
print('O produto que antes custava R${:.2f}, com 5 porcento de desconto, vai para R${:.2f}'.format(preco, preco - desconto)) 
