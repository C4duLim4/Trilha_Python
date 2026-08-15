with open("dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.read().splitlines()

for linha in linhas:
    partes = linha.split(",")
    nome = partes[0]
    preco = float(partes[1])
    quantidade = int(partes[2])
    total = preco * quantidade

    print(nome, total)