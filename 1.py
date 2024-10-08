import random
import numpy as np


def matrizTriangularSuperior(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    triangularSuperior = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if j >= i:
                linha.append(random.randint(-7, 7))
            else:
                linha.append(0)
        triangularSuperior.append(linha)
    
    return triangularSuperior


def matrizTriangularInferior(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    triangularInferior = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if j <= i:
                linha.append(random.randint(-10, 10))
            else:
                linha.append(0)
        triangularInferior.append(linha)
    
    return triangularInferior


def criarMatriz():
    ordem = int(input("Digite a ordem da matriz: "))
    
    
    matriz = np.zeros((ordem, ordem))

   
    triangularSuperior = matrizTriangularSuperior(matriz)
    triangularInferior = matrizTriangularInferior(matriz)

    
    triangularSuperior = np.array(triangularSuperior)
    triangularInferior = np.array(triangularInferior)

    
    print("Matriz Triangular Superior:")
    print(triangularSuperior)
    print("\nMatriz Triangular Inferior:")
    print(triangularInferior)


if __name__ == "__main__":
    criarMatriz()
