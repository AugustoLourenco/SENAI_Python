# DESAFIO 04 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = input("Digite uma frase: ")
frase_maiuscula = frase.upper()

# Quantas vezes aparece a letra "A"
quantidade_letra = frase_maiuscula.count("A")
print(quantidade_letra)
# Ou print(frase_maiuscula.count("A"))


# Em que posição ela aparece a primeira vez
inicio_caracter = frase_maiuscula.find("A")
print(f"A letra A apareceu na posição {inicio_caracter + 1}")

# Em que posição ela aparece a ultima vez
final_caracter = frase_maiuscula.rfind("A")
print(f"A letra A apareceu pela ultima vez na posição {final_caracter + 1}")