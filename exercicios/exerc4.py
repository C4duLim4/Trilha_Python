nomearq = str(input('Digite o nome do arquivo que deseja: '))

contarq = str(input('Digite o conteudo do arquivo: '))

with open(nomearq, 'w') as arquivo:
    arquivo.write(contarq)