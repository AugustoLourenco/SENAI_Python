# DESAFIO 03 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso o CTPS  for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 
# Sabendo que ele vai se aposentar após 35 anos de colaboração.

from datetime import *
data_atual = date.today()
ano_atual = data_atual.year
    
dicionario = {}
lista = list() # Podemos declarar lista dessa maneira

while True:
    
    dicionario["Nome"] = str(input("Digite o nome da pessoa: ")).upper()
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    dicionario["Idade"] = ano_atual - ano_nascimento
    dicionario["CTPS"] = int(input("Digite o numero da CTPS: "))

    if dicionario["CTPS"] != 0:
        dicionario["Ano de Contratação"] = int(input("Digite o ano de contratação: "))
        dicionario["Salário"] = float(input("Digite o salário: "))
        anos_colaboração = ano_atual - dicionario["Ano de Contratação"]
        dicionario["Idade da aposentadoria"] = dicionario["Idade"] + (35 - anos_colaboração)
    
    
    continuar = input("Deseja cadastrar mais pessoas? S ou N: ").upper()
    

    lista.append(dicionario.copy())
    
    if continuar == "N":
        break

print(dicionario)
print(lista)