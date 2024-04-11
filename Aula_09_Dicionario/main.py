meu_dicionario = {
    "Nome" : "Nami",
    "Sobrenome" : "Jafet",
    "Idade" : 67
}

# Acessando todo o dicionário
print(meu_dicionario)

# Acessando os itens do dicionário
print(meu_dicionario.items())

# Acessando os valores do dicionário
print(meu_dicionario.values())

# Acessando as chaves do dicionário
print(meu_dicionario.keys())

# Adicionando itens em um dicionário
meu_dicionario["Cidade"] = "Mogi das Cruzes" 
print(meu_dicionario)

# Alterando itens de um dicionário
meu_dicionario["Idade"] = 100
print(meu_dicionario)

# Deletando itens em um dicionário
del meu_dicionario["Idade"]
print(meu_dicionario)