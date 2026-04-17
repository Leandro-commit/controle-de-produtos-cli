import random

vitorias = 0
derrotas = 0
empates = 0

while True:
    computador = random.choice(["pedra", "papel", "tesoura"])

    print("\nNovo jogo iniciado ▶️")

    jogada = input("\nJogador 01: Pedra, papel ou tesoura? ").lower()
    if jogada not in ["pedra", "papel", "tesoura"]:
        print("Jogada inválida")
        continue

    if jogada == computador:
        print("Empate")
        empates += 1

    elif (
        (jogada == "pedra" and computador == "tesoura")
        or (jogada == "tesoura" and computador == "papel")
        or (jogada == "papel" and computador == "pedra")
    ):
        print("Você ganhou ✅")
        vitorias += 1

    else:
        print("Você perdeu ❌")
        derrotas += 1

    print(f"Vitórias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}")
