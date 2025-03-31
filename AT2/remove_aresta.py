def removeAresta(matriz, vi, vj):
    if matriz[vi][vj] == 0:  # não existe aresta entre vi e vj
        return matriz

    matriz[vi][vj] = 0  # remove a aresta entre vi e vj
    matriz[vj][vi] = 0  # remove a aresta entre vj e vi (grafo não-dirigido)

    return print(matriz)