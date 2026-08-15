from pathlib import Path
dados = []
lista_dicionario = []

with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados.append(linha.strip())

dados.pop(0)

for dado in dados:
    d = dado.split(',')
    lista_dicionario.append({
        "descrição": d[0],
        "data": d[1]
    })

lista_dicionario.pop(0)

with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("descrição, data" + "\n")

with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
    for d in lista_dicionario:
        arquivo.write(f"{d['descrição']}, {d['data']}\n")



