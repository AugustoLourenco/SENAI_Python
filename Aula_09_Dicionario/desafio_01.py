# DESAFIO 01 - Faça  um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

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