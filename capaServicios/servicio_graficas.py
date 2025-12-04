import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from datetime import datetime

def graficar_convergencia(resultados):
    """Servicio de salida: genera gráfico de convergencia"""
    plt.plot(resultados['errores'], marker='o')
    plt.yscale('log')
    plt.xlabel("Iteración")
    plt.ylabel("Error (escala logarítmica)")
    plt.title("Convergencia del Método SSOR")
    plt.grid()
    
    # Guardar la imagen con timestamp único
    ruta = "/home/ZzzZzz/AlgoritmosNumericosParaIngenieria/proyectoSSOR/capaServicios/graficas"
    os.makedirs(ruta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    nombre_archivo = f"convergencia_ssor_{timestamp}.png"
    plt.savefig(os.path.join(ruta, nombre_archivo))
    
    plt.show()
