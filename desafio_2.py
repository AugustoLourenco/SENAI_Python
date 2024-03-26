# DESAFIO 2 - Faça um programa que leia um número inteiro e mostra na tela e seu sucessor e seu antecessor.
numero_usuario = int(input("Digite um valor: "))

numero_sucessor = numero_usuario + 1
numero_antecessor = numero_usuario - 1

print(f"O sucessor de {numero_usuario} é: {numero_sucessor}")
print(f"O antecessor de {numero_usuario} é: {numero_antecessor}")