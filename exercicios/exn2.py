lista = [
    {"arquivo": "nomes.txt", "dados": ["Carlos", "Laura"]},
    {"arquivo": "cidades.txt", "dados": ["Extrema", "São Paulo"]}
]

for item in lista:
    nome_arquivo = item["arquivo"]
    dados = item["dados"]

    with open(nome_arquivo, "w") as arquivo:
        for valor in dados:
            arquivo.write(f"{valor}\n")