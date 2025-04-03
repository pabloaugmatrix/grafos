def dirigido(listaAdjacencias):
    for vertice in listaAdjacencias:
        for adjacente in listaAdjacencias[vertice]:
            if vertice not in listaAdjacencias[adjacente]:
                return True
    return False


def removeArestaLista(listaAdj, vi, vj):
    if not dirigido(listaAdj):
        listaAdj[vj].remove(vi)
    listaAdj[vi].remove(vj)
    print(listaAdj)


if __name__ == "__main__":
    removeArestaLista({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 0, 2)
    removeArestaLista({0: [1, 1, 2, 2, 3, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 0, 1, 2]}, 0, 3)
    removeArestaLista({0: [1, 2, 5], 1: [0, 5], 2: [0, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3], 5: [0, 1, 2, 6], 6: [3, 5]},
                      1, 5)
    removeArestaLista({0: [2], 1: [0, 0, 2], 2: [3], 3: [1]}, 0, 2)
