def somar(a, b):
    return a + b

while True:
    try:
        num1 = float(input('Digite o número1: '))
        break
    except:
        print("Número1 precisa ser número")

while True:
    try:
        num2 = float(input('Digite o número2: '))
        break
    except:
        print("Número2 precisa ser número")

soma = somar(num1, num2)
print(soma)