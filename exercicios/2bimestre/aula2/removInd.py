resultados = []
c = 0

while True:
    opcao = input(''' ----- MENU ------
    1 - fazer conta
    2 - apagar calculo
    3 - mostrar calculos salvos
    4 - sair: ''')

    if opcao == "1":
        comp = float(input("Digite a area do quadrado: "))
        larg = float(input("Digite a altura do quadrado: "))

        resp = comp*larg

        print(resp)

        sn = input('''Deseja salvar o resultado?"
        1 - Sim 
        2 - Não:
                    ''')

        if sn == "1":
            resultados.append({
                    "indice": c,
                    "Comprimento": comp, 
                    "largura": larg
                })
            c += 1
        
        if sn == "2":
            print ("Resposta não salva.")
            
    

    if opcao == "2":
        print(resultados)
        apag = int(input("Escolha o índice de qual calculo apagar: "))
        resultados.pop(apag)

    if opcao == "3":
        if resultados == []:
            print("Lista ainda vazia. Adicione algum calculo ")
        else:
            print(resultados)

    if opcao == "4":
        print("Você saiu!")
        break

        





