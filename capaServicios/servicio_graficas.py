import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from datetime import datetime
import io

def graficar_convergencia(resultados):
    """Servicio de salida: genera gráfico de convergencia y retorna bytes"""
    plt.figure()
    plt.plot(resultados['errores'], marker='o')
    plt.yscale('log')
    plt.xlabel("Iteración")
    plt.ylabel("Error (escala logarítmica)")
    plt.title("Convergencia del Método SSOR")
    plt.grid()
    
    # Guardar en memoria como bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_bytes = buffer.read()
    buffer.close()
    plt.close()
    
    # También guardar en disco (opcional, para respaldo)
    ruta = "/home/ZzzZzz/AlgoritmosNumericosParaIngenieria/proyectoSSOR/capaServicios/graficas"
    os.makedirs(ruta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    nombre_archivo = f"convergencia_ssor_{timestamp}.png"
    
    with open(os.path.join(ruta, nombre_archivo), 'wb') as f:
        f.write(imagen_bytes)
    
    return imagen_bytes
