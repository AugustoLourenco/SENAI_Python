personagens = [
    {
        "Nome" : "Bob",
        "Sobrenome" : "Esponja",
        "Idade" : 10
    },
    
    {
        "Nome" : "Johnny",
        "Sobrenome" : "Bravo",
        "Idade" : 35
    },
    
    {
        "Nome" : "Anakyn",
        "Sobrenome" : "Skywalker",
        "Idade" : 22
    },
    
    {
        "Nome" : "Roronoa",
        "Sobrenome" : "Zoro",
        "Idade" : 16
    }     
]

# Acessando a lista
print(personagens)

# Acessando registro específico
registro_especifico = personagens[2]
print(registro_especifico)
# print(personagens[2])

# Acessando dado específico dentro do registro específico
print(registro_especifico["Nome"])
print(registro_especifico["Sobrenome"])
print(registro_especifico["Idade"])