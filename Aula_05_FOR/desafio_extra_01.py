# Construa um programa em Python utilizando os conhecimentos aprendidos até agora para encontrar todos os numeros pares entre 1 e 100.

inicio = 0
fim = 51
salto = 1

for numeros in range (inicio, fim, salto):
    
    modulo = numeros % 2
    
    if modulo == 0:
        print(numeros)
else:
    print("Acabou")