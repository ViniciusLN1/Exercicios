nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('O seu primeiro nome eh {}'.format(n[0]))
print('O seu ultimo nome eh {}'.format(n[len(n)-1]))
