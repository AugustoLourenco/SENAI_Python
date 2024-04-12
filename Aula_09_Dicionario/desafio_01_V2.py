# DESAFIO 01 - Faça  um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

meuDicionario ={}

meuDicionario['nome']= str(input("Digite seu nome: "))
meuDicionario['nota']= float(input("Digite sua Média: "))


if meuDicionario['nota']>=7:
    meuDicionario['situacao']= "Aprovado"
elif meuDicionario['nota']>=5  and meuDicionario['nota']<7:
    meuDicionario['situacao']= "Recuperação! - Tem salvação!"
else:
    meuDicionario['situacao']= "Reprovado - Se lascou!"
   
print(meuDicionario)

for k, v in meuDicionario.items():
    print(f"O {k} é igual a {v}")
   

# print(f"O Nome é igual a {meuDicionario['nome']}")
# print(f"A Média é igual a {meuDicionario['nota']}")
# print(f"Sua Situação é {meuDicionario['situacao']}")