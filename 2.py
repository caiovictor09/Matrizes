import numpy as np

def escalonar(matriz):
    

    return matriz

def criar_matriz():
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            valor = float(input(f"Digite o elemento[{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    return np.array(matriz)




if __name__ == "__main__":
    pass
