# servidor.py
# Ubicación: ~/AlgoritmosNumericosParaIngenieria/proyectoSSOR/capaInterfaz/servidor.py

from flask import Flask, render_template, request, jsonify
import sys
import os

# Agregar el directorio raíz del proyecto al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from capaControl.control_de_flujo import resolver_sistema

app = Flask(__name__)

@app.route('/')
def index():
    """Ruta principal que muestra la interfaz"""
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    """Endpoint que recibe los datos y ejecuta el método SSOR"""
    try:
        # Obtener datos del request
        datos = request.get_json()
        
        ecuaciones = datos.get('ecuaciones', [])
        omega = datos.get('omega', 1.2)
        tolerancia = datos.get('tolerancia', 1e-4)
        iter_max = datos.get('iter_max', 50)
        
        # Validar que hay ecuaciones
        if not ecuaciones or len(ecuaciones) == 0:
            return jsonify({'error': 'No se proporcionaron ecuaciones'}), 400
        
        # Ejecutar el método SSOR
        resultados = resolver_sistema(ecuaciones, omega, tolerancia, iter_max)
        
        # Convertir arrays numpy a listas para JSON
        respuesta = {
            'matriz': resultados['matriz'].tolist(),
            'vector_b': resultados['vector_b'].tolist(),
            'validaciones': resultados['validaciones'],
            'solucion': resultados['solucion'].tolist(),
            'errores': resultados['errores'],
            'iteraciones_detalle': [
                {
                    'iteracion': detalle['iteracion'],
                    'x_adelante': detalle['x_adelante'].tolist(),
                    'x_atras': detalle['x_atras'].tolist(),
                    'error': detalle['error']
                }
                for detalle in resultados['iteraciones_detalle']
            ]
        }
        
        return jsonify(respuesta)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def iniciar_servidor(host='127.0.0.1', port=5000, debug=True):
    """Función para iniciar el servidor Flask"""
    print(f"\n{'='*60}")
    print(f"Servidor SSOR iniciado")
    print(f"Accede a la aplicación en: http://{host}:{port}")
    print(f"Presiona Ctrl+C para detener el servidor")
    print(f"{'='*60}\n")
    
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    iniciar_servidor()
