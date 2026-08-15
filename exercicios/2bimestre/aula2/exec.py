mensagens = []

for i in range (4):
    message = input ("informe a mensagem")
    mensagens.append(message)
    print('''1 - Sim
          2 - Não''')
    opcao = input("você deseja manter a ultima mensagem? ")

    if opcao == "2":
        mensagens.pop()

for msg in mensagens:
    print(msg)