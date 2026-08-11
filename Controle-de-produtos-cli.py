produtos = []


def mostrar_menu():
    print("===Controle de produtos===\n")
    print("1. Cadastrar produto")
    print("2. Listar ou remover produtos")
    print("3. Buscar produto")
    print("4. SAIR\n")


def cadastrar_produto():

    nome = input("Nome do produto: ")
    while True:
        try:
            preco_conversao = input("Preço: ").replace(",", ".")
            preco = float(preco_conversao)
            if preco <= 0:
                print("Preço inválido")
                continue
            break
        except ValueError:
            print("Digite um valor válido!")

    while True:
        try:
            qtd = int(input("Quantidade: "))
            if qtd <= 0:
                print("Digite uma quantidade acima de 0")
                continue
            break

        except ValueError:
            print("Digite uma quantidade válida!")
            continue

    cadastro = {"nome": nome, "preco": preco, "qtd": qtd}

    produtos.append(cadastro)
    print("\033[92mProduto cadastrado com sucecesso!\n\033[0m")


def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("\033[92m\n===Produto encontrado===\033[m")
            print(
                f"Nome: {produto['nome']} | Preço: {produto['preco']:.2f} | Quantidade: {produto['qtd']}"
            )
            encontrado = True
            break

    if not encontrado:
        print("\033[91mProduto não encontrado\033[0m")


def listar_remover():
    if not produtos:
        print("\nNenhum produto registrado!")
        return

    else:
        print("\nProdutos cadastrados:")
        for i, item in enumerate(produtos, start=1):
            print(
                f"\n{i} - Nome: {item['nome']} | "
                f"Preço: {f'{item['preco']:.2f}'.replace('.', ',')} | "
                f"Quantidade: {item['qtd']}"
            )

        remover = int(
            input("\nDigite 0 para SAIR ou o índice do produto que deseja remover: ")
        )
        if remover >= 1 and remover <= len(produtos):
            produto_removido = produtos.pop(remover - 1)
            print(f"\n{produto_removido['nome']} foi removido do carrinho!\n")

        elif remover == 0:
            print("Voltando ao menu...\n")
            return
        else:
            print("\nNúmero inválido")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao not in range(1, 5):
            print("Opção inválida")
            continue

    except ValueError:
        print("Digite uma opção válida!")
        continue

    if opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        listar_remover()

    elif opcao == 3:
        buscar_produto()

    elif opcao == 4:
        print("Encerrando...")
        break
