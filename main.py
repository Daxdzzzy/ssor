# main.py
# Ubicación: ~/AlgoritmosNumericosParaIngenieria/proyectoSSOR/main.py

from capaControl.control_de_flujo import resolver_sistema, mostrar_resultados, graficar_convergencia

def main():
    # Sistema de ecuaciones
    ecuaciones = [
        "8x1 + x2 = 9",
        "-2x1 + 7x2 - x3 = -5",
        "-x2 + 9x3 = 4"
    ]
    
    # Parámetros del método
    w = 1.2
    tol = 1e-4
    iter_max = 50
    
    # Ejecutar
    resultados = resolver_sistema(ecuaciones, w, tol, iter_max)
    mostrar_resultados(resultados)
    graficar_convergencia(resultados)

if __name__ == "__main__":
    main()
