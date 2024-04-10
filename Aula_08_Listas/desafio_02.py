# DESAFIO 02 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
# No final serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    
    numero_usuario = int(input(f"Digite um número inteiro (0 para sair): "))
    
    if numero_usuario not in lista and numero_usuario != 0:
        lista.append(numero_usuario)
    if numero_usuario == 0:
        break
    
lista.sort()
print(lista)