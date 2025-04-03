def removeVerticeLista(listaAdj, v):
    del listaAdj[v]
    for i in listaAdj:
        while v in listaAdj[i]:
            listaAdj[i].remove(v)
    print(listaAdj)


if __name__ == "__main__":
    removeVerticeLista({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 2)
    removeVerticeLista({0: [1, 1, 2, 2, 3, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 0, 1, 2]}, 0)
    removeVerticeLista({0: [1, 2, 5], 1: [0, 5], 2: [0, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3], 5: [0, 1, 2, 6], 6: [3, 5]},
                       6)
    removeVerticeLista({0: [2], 1: [0, 0, 2], 2: [3], 3: [1]}, 1)
    removeVerticeLista({0: [], 1: [0, 2], 2: [3], 3: [1]}, 0)
    removeVerticeLista({0: [1, 1, 2, 2, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 1, 2]}, 0)
