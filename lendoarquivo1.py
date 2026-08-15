with open ("arquivo1.txt", "w") as arquivo1:
    arquivo1.write("Carlos\n")
    arquivo1.write("Laura\n")
    arquivo1.write("Michi\n")

with open("arquivo1.txt", "r") as a:
    dados = a.read()
    print(dados)

lista = dados.splitlines()

lista.remove("Laura")
print(lista)

for nome in lista:
    with open("arquivo1.txt", "w") as a:
        a.write(f"{nome}\n")


