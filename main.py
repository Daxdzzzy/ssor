# main.py
# Ubicación: ~/AlgoritmosNumericosParaIngenieria/proyectoSSOR/main.py

from capaInterfaz.servidor import iniciar_servidor

if __name__ == "__main__":
    # Iniciar el servidor web
    iniciar_servidor(host='127.0.0.1', port=5000, debug=True)
