# DESAFIO 03 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso o CTPS  for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 
# Sabendo que ele vai se aposentar após 35 anos de colaboração.

senai = {}
lista = list() # Podemos declarar lista dessa maneira

while True:
    
    senai["Nome"] = str(input("Digite o nome do aluno: ")).upper()
    senai["Média"] = float(input("Digite a média do aluno: "))
    continuar = input("Deseja adicionar mais alunos? S ou N: ").upper()

    if senai["Média"] >= 7:
        senai["Situação"] = "Aprovado" 
    else:
        senai["Situação"] = "Reprovado"

    lista.append(senai.copy())
    
    if continuar == "N":
        break

for e in lista: # percorrer cada dicionario
    for v in e.values(): # exibir cada valor
        print(v, end=" // ")
    print(" ")