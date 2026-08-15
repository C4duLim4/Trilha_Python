
while True:
    nome = str(input("Escreva o nome do arquivo: ")).strip()
    est = str(input("Escreva a estenção: ")).strip()
    conteudo = str(input("Escreva o conteudo do arquivo: "))

    with open(f"{nome+'.'+est}", "w") as arq:
        arq.write(conteudo)

    print('''======MENU=====
    1 - Continuar criando arquivos
    2 - Encerrar ''')

    opc = int(input("Digite uma opcão: "))
    
    if opc == 2:
        break
    else:
        pass
