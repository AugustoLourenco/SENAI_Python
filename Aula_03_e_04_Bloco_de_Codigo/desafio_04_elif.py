# DESAFIO 04 - A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL		
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(date.year())
idade =  int(date.year()) - ano_nascimento

if idade > 24:
    print(f"MASTER. {idade} anos.")
elif idade > 19:
    print(f"SÊNIOR. {idade} anos.")
elif idade > 14:
    print(f"JÚNIOR. {idade} anos.")
elif idade > 9:
    print(f"INFANTIL. {idade} anos.")
else:
    print(f"MIRIM. {idade} anos.")