def dirigido(listaAdjacencias):
    for vertice in listaAdjacencias:
        for adjacente in listaAdjacencias[vertice]:
            if vertice not in listaAdjacencias[adjacente]:
                return True
    return False


def calcDensidadeLista(lista):
    vertices = len(lista)
    arestas = 0
    for vertice in lista:
        arestas += len(lista[vertice])
    if not dirigido(lista):
        print(f"{arestas / (vertices * (vertices - 1)):.3}")
    else:
        print(f"{(2 * arestas) / (vertices * (vertices - 1)):.3}")


if __name__ == '__main__':
    calcDensidadeLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]})
    calcDensidadeLista(
        {0: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 17, 19, 21, 31], 1: [0, 2, 3, 7, 13, 17, 19, 21, 30],
         2: [0, 1, 3, 7, 8, 9, 13, 27, 28, 32], 3: [0, 1, 2, 7, 12, 13], 4: [0, 6, 10], 5: [0, 6, 10, 16],
         6: [0, 4, 5, 16], 7: [0, 1, 2, 3], 8: [0, 2, 30, 32, 33], 9: [2, 33], 10: [0, 4, 5], 11: [0], 12: [0, 3],
         13: [0, 1, 2, 3, 33], 14: [32, 33], 15: [32, 33], 16: [5, 6], 17: [0, 1], 18: [32, 33], 19: [0, 1, 33],
         20: [32, 33], 21: [0, 1], 22: [32, 33], 23: [25, 27, 29, 32, 33], 24: [25, 27, 31], 25: [23, 24, 31],
         26: [29, 33], 27: [2, 23, 24, 33], 28: [2, 31, 33], 29: [23, 26, 32, 33], 30: [1, 8, 32, 33],
         31: [0, 24, 25, 28, 32, 33], 32: [2, 8, 14, 15, 18, 20, 22, 23, 29, 30, 31, 33],
         33: [8, 9, 13, 14, 15, 18, 19, 20, 22, 23, 26, 27, 28, 29, 30, 31, 32]})
    calcDensidadeLista({0: [1, 2, 5], 1: [0], 2: [0, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3], 5: [0, 2, 6], 6: [3, 5]})
