# DESAFIO 04 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    
    numero_usuario = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero_usuario != 0:
        lista.append(numero_usuario)
    
    resto = numero_usuario % 2
    if resto == 0 and numero_usuario != 0:
        lista_par.append(numero_usuario)
    elif numero_usuario != 0:
        lista_impar.append(numero_usuario)

    if numero_usuario == 0:
        break

print(f"A lista completa é: {lista}")
print(f"Os números pares são: {lista_par}")
print(f"Os números ímpares são: {lista_impar}")