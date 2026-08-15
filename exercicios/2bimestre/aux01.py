pacientes = []

while True:
    print('''---- MENU ----
        1- Cadastrar um novo usuário na fila
        2- Atender o primeiro usuário da fila
        3- Listar todos os usuários cadastrados na fila
        4- Sair do sistema''')
    
    opc = int(input("O que deseja? "))
    
    if opc == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pacientes.append({"nome": nome,
                          "idade": idade})

    if opc == 2:
        exs = len(pacientes)
        if exs != 0:
            l = input("Qual paciente atender: ")

            pacientes.pop(0)
            print("Atendimento realizado!")
        else:
            print("Lista sem paciente!")

    if opc == 3:
        print(pacientes)

    if opc == 4:
        print("Você saiu do sistema")
        break
    