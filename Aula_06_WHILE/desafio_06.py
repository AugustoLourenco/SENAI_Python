# DESAFIO 06 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 100,00.
# C) Qual é o nome do produto mais barato.

total_compra = 0
produtos_maiores = 0
preço_mais_barato = 100000000000
produto_mais_barato = ""


while True:
    
    produto = input("Digite o produto: ").upper()
    preço = float(input("Digite o  preço do produto: "))
    continuar = input("Deseja adicionar mais itens ao carrinho? S ou N: ").upper()
    total_compra = total_compra + preço
    
    if preço > 100:
        produtos_maiores = produtos_maiores + 1
    else: produtos_maiores = produtos_maiores

    if  preço < preço_mais_barato:
        preço_mais_barato = preço
        produto_mais_barato = produto
    else: 
        preço_mais_barato = preço_mais_barato
        
    if continuar == "N":
        break
print(f"Total da compra: R${total_compra:.2f}")
print(f"{produtos_maiores} produtos custam mais que R$100,00")
print(f"O produto mais barato é o {produto_mais_barato}")  