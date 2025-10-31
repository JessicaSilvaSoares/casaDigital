import csv
import json
from functools import reduce

def main():
    nome_arquivo = input("Digite nome do arquivo: ")

    resultado_final = []

    with open(nome_arquivo, mode="r", encoding='utf-8') as arquivo:
        alunos = list(csv.DictReader(arquivo, delimiter=";"))

    for aluno in alunos:
        aluno["nota1"] = float(aluno["nota1"])
        aluno["nota2"] = float(aluno["nota2"])
        aluno["nota3"] = float(aluno["nota3"])

        aluno["media"] = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
        aluno["aprovado"] = aluno["media"] >= 7

        resultado_final.append(aluno)

    relatorio = {}

    relatorio["quantidade_aprovados"] = len([aluno for aluno in resultado_final if aluno["aprovado"] == True])
    relatorio["quantidade_reprovados"] = len([aluno for aluno in resultado_final if aluno["aprovado"] == False])

    relatorio["media_geral"] = reduce(lambda acc, curr: acc + curr["media"], resultado_final, 0) / len(resultado_final)
    notas = []
    for aluno in resultado_final:
        notas.extend([aluno["nota1"], aluno["nota2"], aluno["nota3"]])
    relatorio["maior_nota"] = reduce(lambda acc, curr: acc if acc > curr else curr, notas)
    relatorio["menor_nota"] = reduce(lambda acc, curr: acc if acc < curr else curr, notas)

    with open("relatorio_notas.json", mode="w") as arquivo:
        writer = json.dump(relatorio, arquivo, indent=4)


if __name__ == "__main__":
    main()
