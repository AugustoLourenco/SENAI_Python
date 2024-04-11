# DESAFIO 03 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na sua posição correta de inserção (sem usar o sort()). 
# No final mostre a lista ordenada na tela 

lista = []

for c in range (0, 5):

    numero_usuario = int(input(f"Digite o {c+1}º número: "))
    
    if c == 0 or numero_usuario > lista[-1]:
        lista.append(numero_usuario)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if numero_usuario <= lista[pos]:
                lista.insert(pos,numero_usuario)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos = pos + 1
            
print(f"Os valores digitados em ordem foram: {lista}")