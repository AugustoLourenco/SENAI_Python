# Variável Local
def funcao_local():
    variavel_local = 10
    print(variavel_local)
    
# funcao_local()
# print(variavel_local) 
# ERRO

# Variável Global

variavel_global = 5

def funcao_global():
    global variavel_global
    variavel_global += 1
    print(variavel_global)

funcao_global()
print(variavel_global)