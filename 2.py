import numpy as np

def criarMatriz():
    ordem = int(input("Digite a ordem da matriz: "))
    matriz = []

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            elemento = None
            while elemento is None:
                try:
                    elemento = int(input(f"Digite o elemento[{i}][{j}]"))   
                except ValueError:
                    print("Digite um valor válido.")


    return matriz

if __name__ == "__main__":
    matriz = criarMatriz()