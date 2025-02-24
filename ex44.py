print('========Lojas americas========')
preco = float(input('Preco das compras: R$'))
print('''Formas de pagamento
[ 1 ] - a vista dinheiro/cartao
[ 2 ] - a vista cartao 
[ 3 ] - 2x no cartao
[ 4 ] - 3x ou mais no cartao
''')
opcao = int(input('Qual a opcao: '))
if opcao == 1:
    desconto = preco * 10 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - desconto))
elif opcao == 2:
    desconto = preco * 5 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - desconto))
elif opcao == 3:
    precoparcela = preco / 2
    print('Sua compra vai custar R${:.2f}.'.format(preco,))
    print('Sua compra vai ser parcelada em 2 vezes de R${:.2f} '.format(precoparcela))

elif opcao == 4:
    parcelas = int(input('Digite quantas parcelas vai ser: '))
    juros = preco * 20 / 100
    precoparcela = (preco + juros) / parcelas
    print('Sua compra vai ser parcelada em {:.2f}x de R${:.2f} COM JUROS'.format(parcelas, precoparcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco + juros))
