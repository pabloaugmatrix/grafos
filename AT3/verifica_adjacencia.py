def verificaAdjacenciaLista(listaAdj, vi, vj):
    print (vj in listaAdj[vi])

if __name__ == "__main__":
    verificaAdjacenciaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 3)
