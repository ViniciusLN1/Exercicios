salario = float(input('Digite o seu salario: '))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('O seu aumento ira ser de 15%, logo ira receber a partir de hoje R${:.2f}'.format(aumento))
elif salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print('O seu aumento ira ser de 10%, logo ira receber a partir de hoje R${:.2f}'.format(aumento))
