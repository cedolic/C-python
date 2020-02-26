salário = float(input('Digite o salário: R$'))
aumento = salário + (salário*15/100)
print('O salário de R${:.2f} com acréscimo de 15% vai para R${:.2f}'.format(salário, aumento))