with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("preço, quantidade\n")
    arquivo.write("20, 2\n")
    arquivo.write("30, 3\n")

# Lê todas as linhas primeiro
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Depois reescreve o arquivo
with open("dados.txt", "w", encoding="utf-8") as arqAberto:
    for linha in linhas:
        valores = linha.split(",")

        if valores[0].strip() == "preço":
            arqAberto.write("preço, quantidade, preco_total\n")
            continue

        preco = float(valores[0].strip())
        quantidade = float(valores[1].strip())

        soma_total = preco * quantidade

        arqAberto.write(f"{preco}, {quantidade}, {soma_total}\n")