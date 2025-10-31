def main():
    lista = []
    index = 1
    while (index <= 50):
        lista.append(index)
        index += 1

    lista_filtrada = [num for num in lista if (num % 3) == 0 or (num % 5) == 0]
    print(f"números encontrados: {lista_filtrada}\n")

    soma = 0
    for num in lista_filtrada:
        soma += num
    print(f"somatório: {soma}")

if __name__ == "__main__":
    main()
