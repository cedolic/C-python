real = float(input('Valor em real: R$ '))
dolar = real/3.27
print('com R${} você pode comparar US${:.2f}'.format(real, dolar))