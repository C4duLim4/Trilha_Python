alunos = []

for i in range(3):
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))

    while True:
        email = input("Email: ").strip()
        repetido = False

        for aluno in alunos:
            if aluno["email"] == email:
                repetido = True
                break

        if email == "":
            print("Email inválido.")
        elif repetido:
            print("Esse email já foi cadastrado.")
        else:
            break

    alunos.append({
        "nome": nome,
        "idade": idade,
        "email": email
    })

with open("email.txt", "w") as arquivo:
    for aluno in alunos:
        arquivo.write(aluno["email"] + "\n")

print(alunos)