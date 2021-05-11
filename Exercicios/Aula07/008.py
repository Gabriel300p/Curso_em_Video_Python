'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''

metro = float(input("Digite a quantidade de metros: "))

cm = metro * 100
mm = cm * 100

print("Em centímetros fica {} e em milimetros {}." .format(cm, mm))