# DESAFIO 04 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

print("Por favor digite 3 números que vou te mostrar qual deles é o maior e qual é o menor")
n1 = int(input("1º numero: "))
n2 = int(input("2º numero: "))
n3 = int(input("3º numero: "))

#print(maior)
if n1 > n2 and n1 > n3:
    print(f"O maior valor foi {n1}")
elif n2 > n3:
    print(f"O maior valor foi {n2}")
else:
    print(f"O maior valor foi {n3}")

#print(menor)
if n1 < n2 and n1 < n3:
    print(f"O menor valor foi {n1}")
if n2 < n3 and n2 < n1:
    print(f"O menor valor foi {n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor valor foi {n3}")