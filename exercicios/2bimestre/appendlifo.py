lista = []

for i in range(2):
    nome = input("Digite um nome: ")
    idade = int(input("Digite sua idade: "))

    lista.append(nome)
    lista.append(idade)

lista.pop()
print(lista)