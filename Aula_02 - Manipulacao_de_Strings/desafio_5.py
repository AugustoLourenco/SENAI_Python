# DESAFIO 05 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente 
# Exemplo: Ana Maria De Souza
# Primeiro: Ana
# Ultimo: Souza

nome = input("Digite seu nome completo: ")
divide_nome = nome.split()
primeiro_nome = divide_nome[0]
ultimo_nome = divide_nome[-1]  

print(f"Nome Completo: {nome}")
print(f"Primeiro: {primeiro_nome}")
print(f"Último: {ultimo_nome}")

# OU

# nome = input("Digite seu nome completo: ")
# divide_nome = nome.split()

# print(f"Nome Completo: {nome}")
# print(f"Primeiro: {divide_nome[0]}")
# print(f"Último: {divide_nome[-1]}")
# total_item = len(divide_nome)
# print(f"Último: {divide_nome[total_item-1]}")