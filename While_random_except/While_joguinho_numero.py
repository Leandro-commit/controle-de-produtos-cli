import random

while True:  # loop do jogo inteiro
    numero_secreto = random.randint(0, 20)
    tentativas = 0
    limite = 5

    print("\nNovo jogo iniciado!")

    while tentativas < limite:
        try:
            chute = int(input("\nAdivinhe o número entre 0 e 20: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        tentativas += 1

        if chute > 20 or chute < 0:
            print("Digite um número entre 0 e 20")

        elif chute > numero_secreto:
            print("Muito alto! Tenta novamente.")

        elif chute < numero_secreto:
            print("Muito baixo! Tenta novamente.")

        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break

        resta = limite - tentativas
        if resta > 0:
            print(f"Você ainda tem {resta} tentativa(s).")
        else:
            print(f"Suas tentativas acabaram! O número era {numero_secreto}")

    # 👇 pergunta se quer jogar novamente
    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").lower()

    if jogar_novamente != "s":
        print("Valeu por jogar! 👋")
        break
