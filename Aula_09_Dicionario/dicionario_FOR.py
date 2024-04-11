# Acessando os itens dentro do dicionário com FOR
# onde o K é a chave e o V é o valor

comidas_favoritas = {
    "comida" : "lanche",
    "suco" : "laranja",
    "refrigerante" : "coca-cola"
}

for k,v in comidas_favoritas.items():
    print(f"O {k} favorito é {v}")