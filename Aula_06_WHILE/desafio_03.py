# DESAFIO 03 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

numeros_digitados = 0
soma = 0
maior = 0
menor = 1000000

while True:
    
    numero_usuario = int(input("Digite um numero: "))
    continuar = input("Deseja continuar? S ou N: ").upper()
    
    numeros_digitados = numeros_digitados + 1
    soma = soma + numero_usuario
    media = soma / numeros_digitados
    
    if numero_usuario > maior:
        maior = numero_usuario
    else:
        maior = maior
        
    if numero_usuario < menor:
        menor = numero_usuario
    else:
        menor = menor
        
    if continuar == "N":
        print("Saindo do loop")
        break
print(f"Foram digitados {numeros_digitados} números. Sendo o maior deles o {maior} e o menor o {menor}.")
print(f"A soma entre eles deu {soma}.")
print(f"A média entre eles deu {media}.")