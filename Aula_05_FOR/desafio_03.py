# DESAFIO 03 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

inicio = 0
fim = 501
salto = 3

soma = 0


for numeros in range (inicio, fim, salto):
    
    modulo =  numeros % 2
    mult_3 = numeros % 3
    
    if modulo != 0:
        print(numeros)
        soma = soma + numeros

else:
    print(f"A soma deu {soma}")