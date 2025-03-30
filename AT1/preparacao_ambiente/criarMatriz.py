import numpy as np

def criar_matriz(instancia):
    caminho = ''+ instancia + '.txt'
    with open(caminho, 'rb') as arquivo:
        matriz = np.genfromtxt(arquivo)
    return matriz
