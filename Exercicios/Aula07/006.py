'''
Monte um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada
'''

numero = int(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print("O dobro do número {} é {}, o triplo {} e a raiz quadrada {:.2f}." .format(numero, dobro, triplo, raiz))