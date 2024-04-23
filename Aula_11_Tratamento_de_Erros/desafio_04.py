try:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    
except ValueError:
    print("DIGITE A SUA IDADE COM VALOR NUMÉRICO")
    
else:
    print(f"CADASTRO CONCLUÍDO")