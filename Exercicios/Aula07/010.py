'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ele pode comprar

Considere
US$1.00 = R$3,27

=(
'''

numero = float(input("Digite a quantidade em reais: "))

print("A quantidade em dolares fica: {:.2f}" .format(numero / 3.27))