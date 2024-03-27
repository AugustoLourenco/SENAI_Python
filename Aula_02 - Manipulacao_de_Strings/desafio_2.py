# DESAFIO 02 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

nome_cidade = input("Digite o nome da cidade: ").upper()
divide_nome = nome_cidade.split()

print("SANTO" in divide_nome[0])