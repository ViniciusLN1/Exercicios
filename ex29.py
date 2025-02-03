velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que era de 80km/h')
    multa = (velocidade - 80) * 7
    print('A multa que voce ira pagar vai ser de R${:.2f}'.format(multa))
print('Tenha um bom dia!')
