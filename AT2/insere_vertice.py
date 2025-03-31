import numpy as np

def insereVertice(matriz):
    n = len(matriz)
    nova_linha = [0] * (n + 1)
    for i in range(n):
        matriz[i].append(0)
    matriz.append(nova_linha)
    return print(np.array(matriz))
