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
    
    return resultados


def mostrar_resultados(resultados):
    """Servicio de salida: imprime los resultados en consola"""
    
    print("\n--- VERIFICACIONES ---")
    print("Matriz A:")
    print(resultados['matriz'])
    print("\nVector b:", resultados['vector_b'])
    
    print("\nSimetría:", "✅ Sí es simétrica" if resultados['validaciones']['es_simetrica'] else "⚠️ NO es simétrica")
    print("Dominancia diagonal:", "✅ Sí es diagonal dominante" if resultados['validaciones']['es_diagonal_dominante'] else "⚠️ NO es diagonal dominante")
    
    print("\n--- Iteraciones del Método SSOR ---\n")
    
    for detalle in resultados['iteraciones_detalle']:
        print(f"Iteración {detalle['iteracion']}:")
        print("   Adelante (SOR):")
        for i in range(len(detalle['x_adelante'])):
            print(f"      x{i+1} = {detalle['x_adelante'][i]:.8f}")
        
        print("   Atrás (SSOR):")
        for i in range(len(detalle['x_atras'])):
            print(f"      x{i+1} = {detalle['x_atras'][i]:.8f}")
        
        print(f"   Error = {detalle['error']:.6e}\n")
    
    print("\n--- Solución Final Aproximada ---")
    for i in range(len(resultados['solucion'])):
        print(f"x{i+1} = {resultados['solucion'][i]:.12f}")
    
    graficar_convergencia(resultados)
