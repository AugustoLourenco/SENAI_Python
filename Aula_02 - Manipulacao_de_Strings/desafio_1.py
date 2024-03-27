# DESAFIO 01 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome em letra maiúscula
# O nome em letra minúscula
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ")
divide_nome = nome.split()
troca_nome = nome.replace(" ", "")

print(nome.upper())
print(nome.lower())
print(len(troca_nome))
print(len(divide_nome[0]))