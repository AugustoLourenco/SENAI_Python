# CRIANDO UM DICIONÁRIO DO ZERO usando lista 

estado = {}
brasil = list() # Podemos declarar lista dessa maneira

for c in range (0, 2):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
    
print(brasil)

for e in brasil: # percorrer cada dicionario
    for v in e.values(): # exibir cada valor
        print(v, end=" ")
    print(" ")