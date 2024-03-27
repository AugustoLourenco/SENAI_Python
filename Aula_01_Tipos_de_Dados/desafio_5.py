# DESAFIO 05 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
# Considere o dólar = R$ 5,00

dinheiro_carteira = float(input("Digite quantos reais voce tem: "))
cotacao_dolar = 5

conversao_dolar = dinheiro_carteira / cotacao_dolar

print(f"Com R$ {dinheiro_carteira}, voce pode comprar U$ {conversao_dolar}")