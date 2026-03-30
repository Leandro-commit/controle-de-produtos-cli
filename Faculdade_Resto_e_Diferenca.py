# *** Par ou ímpar com resto de divisão***

# n1 = int(input("Digite um número: "))
# if n1 % 2 == 0:
#     print("O número é par!")
# else:
#     print("O número é ímpar!")

# ***Diferença com data de nascimento***

# nasc = int(input("Em que ano você nasceu? "))
# ano = 2026

# idade = ano - nasc
# print("Sua idade é:", idade)

# if idade >= 18:
#     print("Parabéns! Você já pode tirar carteira de motorista!")
# else:
#     print("Menores de 18 anos não podem tirar carteira de motorista!")

# ***Pegando o ano automaticamente do PC***

from datetime import datetime

nasc = int(input("Em que ano você nasceu? "))
ano = datetime.now().year

if nasc >= ano:
    print("Ano inválido")
else:
    idade = ano - nasc
    print("Sua idade é", idade)

if idade >= 18:
    print("Você já pode tirar habilitação!")
else:
    print("Menores de 18 anos não pode tirar habilitação!")
