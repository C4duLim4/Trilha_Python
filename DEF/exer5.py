registros = []

def area(comp, larg):
    return comp * larg

def excluirRegistro():
    if not registros:
        print("Nenhum registro encontrado.")
        return

    try:
        excluir = int(input("Qual índice deseja excluir? "))

        for i, registro in enumerate(registros):
            if registro["indice"] == excluir:
                registros.pop(i)
                print("Registro apagado!")
                atualizar_indices()
                return

        print("Índice não encontrado.")

    except ValueError:
        print("Digite um número válido!")

def atualizar_indices():
    for i, registro in enumerate(registros):
        registro["indice"] = i

def Registro():
    comp = float(input("Digite o comprimento: "))
    larg = float(input("Digite a largura: "))

    salvar = input("Deseja salvar? (s/n): ").lower().strip()

    if salvar == "s":
        registros.append({
            "indice": len(registros),
            "Comprimento": comp,
            "Largura": larg,
            "Area": area(comp, larg)
        })

        print("Registro salvo com sucesso!")

while True:

    menu = int(input("""
---- MENU ----
1 - Novo cálculo
2 - Excluir registro
3 - Listar registros
4 - Sair

Escolha: """))

    if menu == 1:
        Registro()

    elif menu == 2:
        excluirRegistro()

    elif menu == 3:
        if not registros:
            print("Nenhum registro cadastrado.")
        else:
            for registro in registros:
                print(registro)

    elif menu == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")