dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
Pd = 60 * dias
Pkm = 0.15 * km
print('O preco a pagar pelo carro eh {:.2f}'.format(Pd + Pkm))
