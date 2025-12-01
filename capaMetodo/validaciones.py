import numpy as np

def es_simetrica(matriz):
    """Verifica si la matriz es simétrica"""
    return np.allclose(matriz, matriz.T)

def es_diagonal_dominante(matriz):
    """Verifica si la matriz es diagonal dominante"""
    for i in range(len(matriz)):
        if abs(matriz[i,i]) < sum(abs(matriz[i,j]) for j in range(len(matriz)) if j != i):
            return False
    return True
