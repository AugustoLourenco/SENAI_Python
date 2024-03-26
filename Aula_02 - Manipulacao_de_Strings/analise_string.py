# Analisando Strings
texto = "Curdo de Python"
nome = "Augusto Pontes Flores Lourenço"

# Conta o número de caractér do texto
print(len(texto))

# Conta o número de caractér do nome
print(len(nome))

# Conta quantas vezes um caractér epecífico aparece no texto
print(texto.count("o"))

# Conta quantas vezes um caractér epecífico aparece no nome
print(nome.count("o"))

# Indica a posição de início de uma frase
print(texto.find("Python"))

# Indica a posição de início do sobrenome
print(nome.find("Lourenço"))

# verificando se possui a palavra em uma frase
print("Python" in texto)
print("Java" in texto)

# verificando se possui a palavra no nome
print("Silva" in nome)
print("Siqueira" in nome)
print("Santos" in nome)
print("Souza" in nome)
print("Ribeiro" in nome)
print("Pontes" in nome)