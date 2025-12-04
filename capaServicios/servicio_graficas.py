import matplotlib.pyplot as plt

def graficar_convergencia(resultados):
    """Servicio de salida: genera gráfico de convergencia"""
    plt.plot(resultados['errores'], marker='o')
    plt.yscale('log')
    plt.xlabel("Iteración")
    plt.ylabel("Error (escala logarítmica)")
    plt.title("Convergencia del Método SSOR")
    plt.grid()
    plt.show()
