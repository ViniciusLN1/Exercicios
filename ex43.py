peso = int(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (metros): '))
imc = peso / (altura * altura)
print('O imc dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif imc <= 25:
    print('Peso Ideal!!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade')
else:
    print('MORBIDA!')
