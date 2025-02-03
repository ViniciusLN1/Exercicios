valor = float(input('Sistema de emprestimo, qual sera o valor da casa? '))
salario = float(input('Valor do salario: '))
anos = float(input('Em quantos anos ira pagar?'))
parcela = valor / (anos * 12)
porcento = salario * 30 / 100
if parcela > porcento:
    print('Emprestimo negado!')
elif parcela <= porcento:
    print('Emprestimo aceito!')
