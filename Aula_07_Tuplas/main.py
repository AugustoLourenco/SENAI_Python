linguagens = ('Assembly', 'Java', 'Python', 'C#')
print(linguagens)

# linguagens = 'Assembly', 'Java', 'Python', 'C#'
# print(linguagens)

lanches = 'Hambúrguer', 'Cerveja', 'Pizza', 'Pudim'

# Chamando item específico:
segundo_item = lanches[1]
print(segundo_item)
# DIRETO -> print(lanches[1])

# Chamando último item:
ultimo_item = lanches[-1]
print(ultimo_item)

# Chamando penultimo item:
penultimo_item = lanches[-2]
print(penultimo_item)

# Acessando mais de um item de uma tupla
dois_itens = lanches[1:3]
print(dois_itens)