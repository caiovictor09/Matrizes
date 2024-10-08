import numpy as np

def criarMatriz():
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(int(input(f"Digite o elemento [{i}][{j}]: ")))
        matriz.append(linha)

    matriz = np.array(matriz)
    return matriz, ordem

def determinante(matriz, ordem):
    if ordem < 0:
        print("Ordem inválida!")
    if ordem == 0:
        return None
    if ordem == 1:
        return matriz[0][0]
    if ordem == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    if ordem == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return (a * (e * i - f * h) 
                - b * (d * i - f * g) 
                + c * (d * h - e * g))
    
    elif ordem >= 3:
        det = 0
        for j in range(ordem):
            submatriz = []
            for linha in range(1,ordem):
                submatriz.append(list(matriz[linha][:j]) + list(matriz[linha][j+1:]))
                
def matrizCofatores(matriz, ordem):
    cofatores = []
    
    for i in range(ordem):
        linha_cofator = []
        for j in range(ordem):
            submatriz = []
            for linha_index in range(ordem):
                if linha_index != i:
                    submatriz.append(list(matriz[linha_index][:j]) + list(matriz[linha_index][j+1:]))
            if len(submatriz) > 0:
                cofator = ((-1) ** (i + j)) * determinante(submatriz, ordem - 1)
            else:
                cofator = 0
            linha_cofator.append(cofator)
        cofatores.append(linha_cofator)
    
    return cofatores

def matrizAdjunta(matriz, ordem):
    cofatores = matrizCofatores(matriz, ordem)
    adjunta = [[cofatores[j][i] for j in range(ordem)] for i in range(ordem)]
    return adjunta

def calcularInversa(det, adjunta):
    inversa = []
    linhas = len(adjunta)
    colunas = len(adjunta[0])
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append((1 / det) * adjunta[i][j])
        inversa.append(linha)
    
    return np.array(inversa)

if __name__ == "__main__":
    matriz, ordem = criarMatriz()
    det = determinante(matriz, ordem)
    
    if det == 0:
        print("Não é possível calcular a inversa. O determinante é zero.")
    else:
        adjunta = matrizAdjunta(matriz, ordem)
        inversa = calcularInversa(det, adjunta)
        print(f"O determinante é {det}.")
        print("Matriz inversa abaixo:")
        print(inversa)
