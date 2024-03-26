# DESAFIO EXTRA 5: Crie um programa que dados o valor, a taxa e o tempo, efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula: 
# prestação = valor + (valor*(taxa/100)*tempo)

valor = float(input("Digite o valor: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = float(input("Digite o tempo: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"O valor da prestação em atraso é: R${prestacao}")