# Transformando uma String
frase = "Microsoft Power BI"

# Trocando uma palavra
troca_palavra = frase.replace("Power BI", "AZ-900")
print(troca_palavra)

# Converter todas as letras para maíusculo
print(frase.upper())

# Converter todas as letras para minúsculo
print(frase.lower())

# Converter a primeira letra da frase para maíusculo
print(frase.capitalize())

# Converter a primeira letra de cada palavra da frase para maíusculo
print(frase.title())

# Removendo espaços inadequados
curso_espacado = "      Fundamentos da Ciência de Dados - Google Cloud          " 
curso = curso_espacado.strip()
print(curso)

# Removendo espaços da direita
curso = curso_espacado.rstrip()
print(curso)

# Removendo espaços da esquerda
curso = curso_espacado.lstrip()
print(curso)