# DESAFIO 05 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Sofa' , 800.00 , 'Geladeira' , 700.00, 'Fogão' , 700.00 , 'Forno' , 300.00)
tamanho = len(produtos)

for i in range (0, tamanho, 2):
    print(f"{produtos[i]:.<30}....R${produtos[i + 1]}")