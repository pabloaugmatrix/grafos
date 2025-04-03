def dirigido(listaAdjacencias):
    for vertice in listaAdjacencias:
        for adjacente in listaAdjacencias[vertice]:
            if vertice not in listaAdjacencias[adjacente]:
                return True
    return False

def insereArestaLista(listaAdjacencias, vi, vj):
    if not dirigido(listaAdjacencias):
        listaAdjacencias[vj].append(vi)
        listaAdjacencias[vj].sort()
    listaAdjacencias[vi].append(vj)
    listaAdjacencias[vi].sort()
    print(listaAdjacencias)

if __name__ == "__main__":
    insereArestaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)
    insereArestaLista({0: [1, 1, 2, 2, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 1, 2]}, 0, 3)
    insereArestaLista({0: [1, 2, 5], 1: [0], 2: [0, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3], 5: [0, 2, 6], 6: [3, 5]}, 1, 5)
    insereArestaLista({0: [], 1: [0, 2], 2: [3], 3: [1]}, 0, 3)
    insereArestaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)






