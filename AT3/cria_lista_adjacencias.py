import numpy as np

def criaListaAdjacencias(matriz):
    dict = {}
    linhas, colunas = np.shape(matriz)
    for linha in range(linhas):
        lista = []
        for coluna in range(colunas):
            if matriz[linha][coluna] > 0:
                for adjacencia in range(matriz[linha][coluna]):
                    lista.append(coluna)
        dict[linha] = lista
    print(dict)

if __name__ == "__main__":
    criaListaAdjacencias([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
