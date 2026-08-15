lista = [
    {
        "arquivo": "nome.txt",
        "dados": ["Carlos","Pedro"]
    },
    {
        "arquivo": "cidades.txt",
        "dados": ["Extrema","São Paulo"]
    }
]

for d in lista:
    with open(d["arquivo"], "w") as arquivo:
        for cidade in d["dados"]:
            arquivo.write(f"{cidade}\n")
