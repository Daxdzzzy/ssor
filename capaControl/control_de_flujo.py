import numpy as np

def resolver_sistema(lista_ecuaciones, w=1.2, tol=1e-4, iter_max=50):
    """Coordina el flujo entre traducción, método y servicios de salida"""
    
    from capaTraduccion.parseador_ecuaciones import convertir_a_matriz
    from capaMetodo.validaciones import es_simetrica, es_diagonal_dominante
    from capaServicios.servicio_bd import ServicioBD
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
    
    # 5. Generar gráfica y obtener bytes
    imagen_bytes = graficar_convergencia(resultados)
    
    # 6. Guardar en base de datos
    try:
        servicio_bd = ServicioBD()
        
        # Convertir numpy arrays a listas para JSON
        matriz_json = matriz.tolist() if isinstance(matriz, np.ndarray) else matriz
        vector_b_json = vector_b.tolist() if isinstance(vector_b, np.ndarray) else vector_b
        solucion_json = solucion.tolist() if isinstance(solucion, np.ndarray) else solucion
        
        # Convertir iteraciones_detalle (arrays numpy a listas)
        iteraciones_para_bd = []
        for iter_dict in iteraciones_detalle:
            iter_copia = iter_dict.copy()
            iter_copia['x_adelante'] = iter_copia['x_adelante'].tolist()
            iter_copia['x_atras'] = iter_copia['x_atras'].tolist()
            iteraciones_para_bd.append(iter_copia)
        
        # Guardar en BD
        id_registro = servicio_bd.guardar_ejecucion(
            matriz_a=matriz_json,
            vector_b=vector_b_json,
            omega=w,
            tolerancia=tol,
            iter_max=iter_max,
            solucion=solucion_json,
            errores=errores,
            iteraciones_detalle=iteraciones_para_bd,
            imagen_binaria=imagen_bytes
        )
        
        print(f"✓ Ejecución guardada en BD con ID: {id_registro}")
        resultados['id_bd'] = id_registro
        
    except Exception as e:
        print(f"⚠ Error al guardar en BD: {e}")
        resultados['id_bd'] = None

    return resultados
