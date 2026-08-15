cesta = []

while True:
    opcao = (input('''-------- MENU -------
          1 - Cadastrar produto a compra
          2 - Deletar produto
          3 - Mostrar Lista
          4 - Sair:   '''))
    
    if opcao == "1":
        prod = str(input("Digite o produto: "))
        preco = float(input("Digite o preço: "))

        cesta.append({
            "produto": prod,
            "preço": preco 
        })

    if opcao == "2":
        if cesta == []:
            print("Lista ainda vazia. Adicione ")  
        else:  
            cesta.pop()
            print("Ultimo cadastro apagado! ")


    if opcao == "3":
        print(cesta)

    if opcao == "4":
        print("Você saiu das compras")
        break


