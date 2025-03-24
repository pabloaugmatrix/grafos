package test

import (
	at2 "extra/src"
	"testing"
)

func TestVerificaAdjacencia(t *testing.T) {
	matriz := [][]int{
		{0, 1, 0, 0},
		{1, 0, 1, 1},
		{0, 1, 0, 1},
		{0, 1, 1, 0},
	}
	verticeI := 0
	verticeJ := 3

	resultado := at2.VerificaAdjacencia(matriz, verticeI, verticeJ)
	esperado := false

	if resultado != esperado {
		t.Errorf("verificaAdjacencia(matriz, verticeI, verticeJ) = %t; esperado %t", resultado, esperado)
	}
}
