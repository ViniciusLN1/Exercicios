from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
conta = atual - ano
if conta == 18:
    print('Você tem {} anos, ja pode alistar!'.format(conta))
elif conta < 18:
    print('Você tem {} anos, falta {} anos!'.format(conta, 18 - conta))
elif conta > 18:
    print('Você tem {} anos, ja passou {} anos!'.format(conta, conta - 18))
