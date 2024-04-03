# DESAFIO 05 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

inicio = 1
fim = 7
salto = 1

soma = 0

for elemento in range (inicio, fim, salto):
    numero_usuario = int(input(f"Digite o {elemento}º número: "))
    
    modulo = numero_usuario % 2
    
    if modulo == 0:
        soma = soma + numero_usuario
    
else:
    print(f"A soma deu {soma}")