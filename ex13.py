salario = float(input('Qual o seu salario atual? '))
aumento = salario*15/100
print('O seu salario de R${:.2f} vai passar para R${:.2f} apos o aumento de 15%'.format(salario, salario+aumento))
