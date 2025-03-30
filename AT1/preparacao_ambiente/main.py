import sys
from criarMatriz import criar_matriz
from obterDimensao import obter_dimensao
from resultado import resultado

def main(instancia):
    matriz = criar_matriz(instancia)
    dimensao = obter_dimensao(matriz)
    resultado(instancia, dimensao) 

if __name__ == '__main__':
    main(str(sys.argv[1]))
