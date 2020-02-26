10*5/100
1500*10/100
875*15/100

preço = float(input('Qual é o preço do produto? R$'))
desconto = preço - (preço*5/100)
print('O preço de {:.2f} com 5% de desconto é {:.2f}'.format(preço, desconto))