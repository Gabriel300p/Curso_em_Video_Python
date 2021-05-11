'''
Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor
'''

numero = int(input("Digite um número: "))

numero1 = numero + 1
numero2 = numero - 1

print("O antecessor de {} é {}, e o sucessor é {}." .format(numero, numero2, numero1))
