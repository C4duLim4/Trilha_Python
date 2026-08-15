from pathlib import Path

arquivo = Path("usuarios.txt")

# Pergunta quantos usuários serão cadastrados
while True:
    try:
        quantidade = int(input("Quantos usuários deseja cadastrar? "))
        if quantidade > 0:
            break
        else:
            print("Digite um número maior que zero.")
    except ValueError:
        print("Digite um número válido.")

# Abre o arquivo no modo de escrita (sobrescreve o arquivo)
with open(arquivo, "w", encoding="utf-8") as f:
    
    for i in range(quantidade):
        while True:
            nome = input(f"Digite o nome do usuário {i+1}: ").strip()
            
            # Validação: nome não pode ser vazio e deve conter apenas letras e espaços
            if nome and all(parte.isalpha() for parte in nome.split()):
                f.write(nome + "\n")
                break
            else:
                print("Nome inválido! Digite apenas letras e não deixe vazio.")

print("Usuários cadastrados com sucesso!")