package at2

func VerificaAdjacencia(matriz [][]int, verticeI int, verticeJ int) bool {
	return matriz[verticeI][verticeJ] != 0
}
