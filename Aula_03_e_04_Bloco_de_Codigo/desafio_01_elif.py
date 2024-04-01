# DESAFIO 01 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digiete o salário do comprador: "))
tempo_compra = float(input("Digite em quantos anos realizará o pagamento: "))
taxa = 0.30
parcela_maxima_comprador = taxa * salario_comprador

prestacao_mensal = valor_casa / (tempo_compra*12)
 
if prestacao_mensal > parcela_maxima_comprador:
    print("Emprétimo negado!")
else:
    print(f"Empréstimo aprovado! Prestação mensal de {prestacao_mensal}")