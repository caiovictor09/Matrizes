import numpy as np

def escalonar_gauss_jordan(matrizA):
    n = len(matrizA)
    
    for k in range(n):
        
        pivo = matrizA[k][k]
        if pivo == 0:
            for i in range(k + 1, n):
                if matrizA[i][k] != 0:
                    
                    matrizA[k], matrizA[i] = matrizA[i], matrizA[k]
                    pivo = matrizA[k][k]
                    break
            if pivo == 0:
                print("A matriz é singular, não pode ser escalonada completamente.")
                return matrizA

        
        matrizA[k] = matrizA[k] / matrizA[k][k]

        
        for i in range(n):
            if i != k:
                fator = matrizA[i][k]
                matrizA[i] = matrizA[i] - fator * matrizA[k]

        
        matrizA[np.isclose(matrizA, 0)] = 0

    return matrizA

def criarMatriz():
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            elemento = None
            while elemento is None:
                try:
                    elemento = float(input(f"Digite o elemento[{i}][{j}]: "))   
                except ValueError:
                    print("Digite um valor válido.")
            linha.append(elemento)
        matriz.append(linha)

    return np.array(matriz)

def escalonarMatriz():
    matrizA = criarMatriz()
    matrizA = escalonar_gauss_jordan(matrizA)

    print("Matriz A escalonada (forma de Gauss-Jordan):")
    print(matrizA)

if __name__ == "__main__":
    escalonarMatriz()
