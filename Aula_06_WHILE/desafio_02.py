# DESAFIO 02 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

parada = 999
numeros_digitados = 0
soma = 0

while True:
    
    numero_usuario = int(input("Digite um numero: "))
    numeros_digitados = numeros_digitados + 1
    soma = soma + numero_usuario
    
    if numero_usuario == parada:
        print("Saindo do loop")
        break
print(f"Foram digitados {numeros_digitados - 1} números. A soma entre eles deu {soma - parada}.")