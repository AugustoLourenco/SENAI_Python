numeros = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))

print(f"O valor 9 apareceu {numeros.count(9)} vezes")

if 3 in numeros:
    print(f"O valor 3 esta na {numeros.index(3)+1}º posição")
else:
    print(f"O valor 3 não aparece nessa tupla")
    
print(f"Os valores pares são ", end='')

for n in numeros:
    resto = n % 2
    if resto == 0:
        print(n, end=' ')