# DESAFIO 06 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. 
# No final mostre os valores pares e impares e ordem crescente.

lista = []

for c in range (0, 7):

    numero_usuario = int(input(f"Digite o {c+1}º número: "))
    
    resto = numero_usuario % 2
    
    