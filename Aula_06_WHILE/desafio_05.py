# DESAFIO 05 - Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

maior_idade = 0
homens_cadastrados = 0
mulheres_menor_20 = 0

while True:
    
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa. M ou F: ").upper()
    continuar = input("Deseja continuar? S ou N: ").upper()
    
    if idade >= 18:
        maior_idade = maior_idade + 1
    else: maior_idade = maior_idade

    if sexo == "M":
        homens_cadastrados = homens_cadastrados + 1
    else: homens_cadastrados = homens_cadastrados

    if idade < 20 and sexo == "F":
        mulheres_menor_20 = mulheres_menor_20 + 1
    else: mulheres_menor_20 = mulheres_menor_20

    if continuar == "N":
        break
print(f"Maior de 18 anos: {maior_idade}")
print(f"Homens cadastrados: {homens_cadastrados}")
print(f"Mulheres com menos de 20 anos: {mulheres_menor_20}")    