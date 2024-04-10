produtos = ('Sofa', 800.00, 'Geladeira', 700.00, 'Fogão', 700.00)
tamanho = len(produtos)



for i in range (0, tamanho, 2):
    print(f"{produtos[i]:.<30}")