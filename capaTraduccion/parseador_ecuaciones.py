import numpy as np
import re

def convertir_a_matriz(lista_ecuaciones):
    """Interpreta las ecuaciones escritas por el usuario y las convierte a formato matricial"""
    variables = sorted(set(re.findall(r'x\d+', ' '.join(lista_ecuaciones))), key=lambda x: int(x[1:]))
    n = len(variables)
    matriz = np.zeros((n, n), dtype=float)
    vector_b = np.zeros(n, dtype=float)

    for i, ecuacion in enumerate(lista_ecuaciones):
        izquierda, derecha = ecuacion.split('=')
        vector_b[i] = float(derecha)
        for var in variables:
            coef = re.findall(rf'([+-]?\s*\d*\.?\d*)\s*{var}', izquierda)
            if coef:
                c = coef[0].replace(' ', '')
                if c in ('', '+'): c = 1
                elif c == '-': c = -1
                matriz[i, int(var[1:]) - 1] = float(c)
    return matriz, vector_b
