import numpy as np

def escalonar_matriz(matriz):
    linhas, colunas = matriz.shape
    for i in range(linhas):
        if matriz[i, i] == 0:
            continue

        # Zerando os valores abaixo do pivô
        for j in range(i + 1, linhas):
            fator = matriz[j, i] / matriz[i, i]
            matriz[j] = matriz[j] - fator * matriz[i]

    return matriz

def main():
    # Entrada do usuário
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = np.zeros((ordem, ordem))

    # Preenchendo a matriz
    print("Digite os elementos da matriz:")
    for i in range(ordem):
        matriz[i] = list(map(float, input(f"Digite os elementos da linha {i + 1}: ").split()))

    # Exibindo a matriz escalonada
    matriz_escalonada = escalonar_matriz(matriz)
    print("Matriz escalonada:")
    print(matriz_escalonada)

if __name__ == "__main__":
    main()
