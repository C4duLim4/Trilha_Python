pilha_livros = []

while True:

    print("\n=== GERENCIADOR DE LIVROS ===")
    print("1 - Adicionar livro")
    print("2 - Remover último livro")
    print("3 - Listar livros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")

        pilha_livros.append({
            "titulo": titulo,
            "autor": autor
        })

        print("Livro adicionado com sucesso!")

    elif opcao == "2":

        if not pilha_livros:
            print("A pilha está vazia.")
        else:
            removido = pilha_livros.pop()

            print("\nLivro removido:")
            print(f"Título: {removido['titulo']}")
            print(f"Autor: {removido['autor']}")

    elif opcao == "3":

        if not pilha_livros:
            print("Nenhum livro cadastrado.")
        else:
            print("\n=== LIVROS NA PILHA ===")

            for i, livro in enumerate(pilha_livros):
                print(f"\nLivro {i + 1}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")

    elif opcao == "4":

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")