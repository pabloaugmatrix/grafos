def calcDensidade(matriz):
    num_vertices = len(matriz)
    num_arestas = sum(sum(linha) for linha in matriz) // 2
    densidade = num_arestas / (num_vertices * (num_vertices - 1) / 2)
    return print(round(densidade, 3))