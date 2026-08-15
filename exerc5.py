tarefas = []

with open("tarefas.txt", "r") as arquivo:
    for linha in arquivo:
        tarefas.append(linha.strip())


while True:
    opc = input('''===== MENU ======
1 - Digitar nova tarefa
2 - Mostrar tarefas
3 - Remover tarefa
4 - Sair: ''')
    
    if opc == '1':
        tar = input("Digite a tarefa: ")
        tarefas.append(tar)

        with open ("tarefas.txt", "a") as arquivo:
            arquivo.write(tar)

        print("Tarefa adicionada!")

    if opc == '2':
        if tarefas == []:
            print("Lista ainda vazia")
        else:
            print(tarefas)

    if opc == '3':
        quant = len(tarefas)
        if tarefas == []:
            print("Lista ainda vazia")
        else:
            tarefas.pop()
            print("Tarefa removida!")

    if opc == '4':
        break
    