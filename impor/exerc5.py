lista = [{
    "arquivo": "nomes.txt",
    "dados": ["Carlos","Pedro"]},
    {
    "arquivo": "cidades.txt",
    "dados": ["Extrema","São Paulo"]}]


for d in lista:
    with open(d["arquivo"], "w", encoding="utf-8") as arquivo:
        for dados in d["dados"]:
            arquivo.write(f"{dados}\n")

