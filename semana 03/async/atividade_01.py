import re
import json

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")

    with open(nome_arquivo, "r") as arquivo : 
        linhas = arquivo.readlines()
        nomes = [re.sub(r"\n$", "", nome) for nome in linhas]

    obj = {}

    obj["total_palavras"] = len(nomes)
    obj["palavras_grandes"] = len([nome for nome in nomes if len(nome) > 5])
    obj["porcentagem"] = obj["palavras_grandes"] / obj["total_palavras"] * 100

    with open("resultado_nomes.json", "w") as arquivo:
        json.dump(obj, arquivo, indent=4)


if __name__ == "__main__":
    main()
