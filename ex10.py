REAL = float(input('Quanto dinheiro voce tem?: '))
US = REAL / 6.04
print('Com R${} voce pode comprar U${:.2f} dollares.'.format(REAL, US))
