

def tipoGrafo(matriz):
    # Verifica se a matriz é quadrada
    if len(matriz) != len(matriz[0]):
        return print("None")

    n = len(matriz)  # Número de vértices

    # Contadores para as ocorrências de arestas e arestas dirigidas
    arestas = 0
    arestas_dir = 0

    # Verifica se há laços e múltiplas arestas
    laço = False
    mult_arestas = False

    # Percorre a matriz
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != 0:  # Se existe uma aresta
                arestas += 1

                if i == j:  # Se é um laço
                    laço = True

                if matriz[j][i] != matriz[i][j]:  # Se a aresta é dirigida
                    arestas_dir += 1

                if matriz[i][j] > 1:  # Se há múltiplas arestas
                    mult_arestas = True

    # Verifica o tipo de grafo
    if laço:
        if arestas_dir > 0:
            return print("31")  # Pseudografo dirigido
        else:
            return print("30")  # Pseudografo
    elif arestas_dir > 0:
        if mult_arestas:
            return print("21")  # Multigrafo dirigido
        else:
            return print("1")  # Digrafo
    else:
        if mult_arestas:
            return print("20")  # Multigrafo
        else:
            return print("0")  # Grafo simples

