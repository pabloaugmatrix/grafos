import numpy as np


def removeVertice(matriz, v):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == v or j == v:
                matriz[i][j] = -1

    return print(np.array(matriz))