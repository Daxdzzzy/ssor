import numpy as np

def ejecutar_ssor(matriz, vector_b, w=1.2, tol=1e-4, iter_max=50):
    """Ejecuta el método numérico SSOR y retorna la solución y los errores"""
    n = len(vector_b)
    x = np.zeros(n)
    errores = []
    iteraciones_detalle = []

    for k in range(iter_max):
        x_anterior = x.copy()

        # Adelante (SOR)
        for i in range(n):
            suma = np.dot(matriz[i, :i], x[:i]) + np.dot(matriz[i, i+1:], x_anterior[i+1:])
            x[i] = (1-w)*x_anterior[i] + (w/matriz[i,i])*(vector_b[i] - suma)

        x_adelante = x.copy()

        # Atrás (SSOR)
        for i in reversed(range(n)):
            suma = np.dot(matriz[i, :i], x[:i]) + np.dot(matriz[i, i+1:], x[i+1:])
            x[i] = (1-w)*x_adelante[i] + (w/matriz[i,i])*(vector_b[i] - suma)

        error = np.linalg.norm(x - x_anterior, np.inf)
        errores.append(error)
        
        iteraciones_detalle.append({
            'iteracion': k+1,
            'x_adelante': x_adelante.copy(),
            'x_atras': x.copy(),
            'error': error
        })

        if error < tol:
            break

    return x, errores, iteraciones_detalle
