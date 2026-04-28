while True:

    print("Olá, o que deseja comprar:")
    print("1 - Coxinha R$ 5,00")
    print("2 - Pastel R$ 7,00")
    print("3 - Café R$ 4,00")
    print("4 - Suco R$ 6,00")
    print("5 - SAIR")

    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha > 5:
            print("Opção númerica inexistente!")
    except ValueError:
        print("Escolha uma opção entre 1 e 5.")
        continue

    if escolha in (1, 2, 3, 4, 5):
        try:
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("Digite apenas uma quantidade númerica!")

        if escolha == 1:
            print(f"Total: {qtd * 5}")

        elif escolha == 2:
            print(f"Total: {qtd * 7}")

        elif escolha == 3:
            print(f"Total: {total * 4}")
