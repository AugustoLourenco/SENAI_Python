# Faça um programa em python utilizando "for" que leia 10 valores inteiros e:
# Encontre e mostre o maior valor
# Encontre e mostre o menor valor
# Calcule e mostre a média dos números lidos

inicio = 1
fim = 11
salto = 1

soma = 0    
maior = 0

for elemento in range (inicio, fim, salto):
    numero_usuario = int(input(f"Digite o {elemento}º número: "))
    
    soma = soma + numero_usuario
    media = soma / (fim - inicio)
    
    if numero_usuario > maior:
        maior = numero_usuario
    else:
        maior = maior
    
    
else:
    print(maior)
    print(f"A média é {media}")