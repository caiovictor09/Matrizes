import numpy as np

def criarMatriz():
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(int(input(f"Digite o elemento [{i}][{j}]: ")))
        matriz.append(linha)

    return matriz

if __name__ == "__main__":
    matriz = criarMatriz()