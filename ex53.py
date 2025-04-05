frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase {} ao contrario e {}'.format(junto, inverso))
if inverso == junto:
    print('PALINDROMO!!!!')
elif inverso != junto:
    print('NAO PALINDROMO!!!!')
    