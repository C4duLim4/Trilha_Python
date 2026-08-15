lista=[]

for user in range(2):
    nome = str(input(f"Informe seu nome usuário {user+1}: "))
    idade = int(input(f"Informe sua idade usuário {user+1}: "))
    filmes = []
    for f in range(5):
        filme = str(input(f"Informe o filme {f+1} usuário {user+1}: "))
        filmes.append(filme)
    
    lista.append(
        {
            "nome": nome,
            "idade": idade,
            "filmes": filmes
        }
    )
    

print(lista)