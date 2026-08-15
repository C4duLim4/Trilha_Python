from pathlib import Path

lista = ["arquivo1.txt","arquivo2.txt"]


for a in lista:
    if lista(a):
        with open(a, "x") as arquivo:
            pass

for a in lista:    
    arquivo = Path(lista[a])

if arquivo.exists():
    print("Arquivo já existe")
else:
    print("Arquivo no existe")