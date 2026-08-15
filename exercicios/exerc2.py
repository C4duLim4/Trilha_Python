with open('numeros.txt', 'w') as arquivo:
    pass

for i in range(3):
    num = int(input(f'Digite o {i+1}° número: '))
    with open('numeros.txt', 'a') as arquivo:
        arquivo.write(f'{num}\n')

