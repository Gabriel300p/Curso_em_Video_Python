'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
'''

numero = float(input("Digite o preço do produto: "))

desconto =  numero * 0.05

print("Com o desconto o produto fica {}" .format(numero - desconto))
