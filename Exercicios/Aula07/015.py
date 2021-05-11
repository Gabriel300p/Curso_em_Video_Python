'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado
'''

km = float(input("Insira a quantidade km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

print("O valor fica de >>> R${}" .format((km * 0.15) + (dias * 60)))