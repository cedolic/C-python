km = float(input('quantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))