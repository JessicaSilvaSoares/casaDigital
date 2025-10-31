def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if (b == 0):
        print("\nImpossível dividir por zero!")
        return None 
    return a / b


if __name__ == "__main__":
    while (True):
        num_1 = input("Digite o primeiro número: ")
        try:
            num_1 = float(num_1)
            break
        except:
            print("Valor inválido, digite novamente!")

    while (True):
        num_2 = input("Digite o segundo número: ")
        try:
            num_2 = float(num_2)
            break
        except:
            print("Valor inválido, digite novamente!")

    while (True):
        operador = input("Digite o operador (+, -, *, /): ")
        if (operador not in "+-*/"):
            print("operador inválido")
            continue
        break

    resultado = None

    match (operador):
        case "+":
            resultado = somar(num_1, num_2)
        case "-":
            resultado = subtrair(num_1, num_2)
        case "*":
            resultado = multiplicar(num_1, num_2)
        case "/":
            resultado = dividir(num_1, num_2)
        case _:
            print("\nOperador inválido!")

    if resultado != None:
        print(f"\n{resultado}")

