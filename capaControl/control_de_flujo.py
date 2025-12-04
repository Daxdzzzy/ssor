import numpy as np

def resolver_sistema(lista_ecuaciones, w=1.2, tol=1e-4, iter_max=50):
    """Coordina el flujo entre traducción, método y servicios de salida"""
    
    from capaTraduccion.parseador_ecuaciones import convertir_a_matriz
    from capaMetodo.validaciones import es_simetrica, es_diagonal_dominante
    from capaMetodo.ssor import ejecutar_ssor
    from capaServicios.servicio_graficas import graficar_convergencia 
    
    # 1. Traducir ecuaciones a formato matricial
    matriz, vector_b = convertir_a_matriz(lista_ecuaciones)
    
    # 2. Validar matriz
    validaciones = {
        'es_simetrica': es_simetrica(matriz),
        'es_diagonal_dominante': es_diagonal_dominante(matriz)
    }
    
    # 3. Ejecutar método numérico
    solucion, errores, iteraciones_detalle = ejecutar_ssor(matriz, vector_b, w, tol, iter_max)
    
    # 4. Preparar resultados
    resultados = {
        'matriz': matriz,
        'vector_b': vector_b,
        'validaciones': validaciones,
        'solucion': solucion,
        'errores': errores,
        'iteraciones_detalle': iteraciones_detalle
    }
    
    graficar_convergencia(resultados)

    return resultados

