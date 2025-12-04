import psycopg2
from psycopg2.extras import Json
import json

class ServicioBD:
    def __init__(self):
        self.config = {
            'dbname': 'ssor_db',
            'user': 'ssor',
            'password': 'ssor123',
            'host': 'localhost',
            'port': '5432'
        }
    
    def conectar(self):
        """Establece conexión con PostgreSQL"""
        return psycopg2.connect(**self.config)
    
    def crear_base_datos(self):
        """Crea la base de datos ssor_db si no existe"""
        try:
            # Conectar a postgres para crear la BD
            conn = psycopg2.connect(
                dbname='postgres',
                user='ssor',
                password='ssor123',
                host='localhost',
                port='5432'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            
            # Verificar si existe
            cursor.execute("SELECT 1 FROM pg_database WHERE datname='ssor_db'")
            exists = cursor.fetchone()
            
            if not exists:
                cursor.execute('CREATE DATABASE ssor_db')
                print("Base de datos 'ssor_db' creada exitosamente")
            else:
                print("Base de datos 'ssor_db' ya existe")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al crear base de datos: {e}")
    
    def crear_tablas(self):
        """Crea las tablas necesarias"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Tabla para guardar ejecuciones del método SSOR
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ejecuciones_ssor (
                id SERIAL PRIMARY KEY,
                fecha_ejecucion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                matriz_a JSON NOT NULL,
                vector_b JSON NOT NULL,
                omega FLOAT NOT NULL,
                tolerancia FLOAT NOT NULL,
                iter_max INTEGER NOT NULL,
                solucion JSON NOT NULL,
                errores JSON NOT NULL,
                iteraciones_detalle JSON NOT NULL,
                grafica BYTEA,
                num_iteraciones INTEGER NOT NULL
            )
        ''')
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Tablas creadas exitosamente")
    
    def guardar_ejecucion(self, matriz_a, vector_b, omega, tolerancia, iter_max, 
                          solucion, errores, iteraciones_detalle, imagen_binaria):
        """Guarda una ejecución completa del método SSOR"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO ejecuciones_ssor 
            (matriz_a, vector_b, omega, tolerancia, iter_max, solucion, 
             errores, iteraciones_detalle, grafica, num_iteraciones)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        ''', (
            Json(matriz_a),
            Json(vector_b),
            omega,
            tolerancia,
            iter_max,
            Json(solucion),
            Json(errores),
            Json(iteraciones_detalle),
            psycopg2.Binary(imagen_binaria),
            len(errores)
        ))
        
        id_registro = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        
        return id_registro
    
    def obtener_historial(self, limite=10):
        """Obtiene el historial de ejecuciones (sin la imagen por eficiencia)"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, fecha_ejecucion, matriz_a, vector_b, omega, 
                   tolerancia, iter_max, solucion, num_iteraciones
            FROM ejecuciones_ssor
            ORDER BY fecha_ejecucion DESC
            LIMIT %s
        ''', (limite,))
        
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return resultados
    
    def obtener_ejecucion_completa(self, id_ejecucion):
        """Obtiene una ejecución completa incluyendo la gráfica"""
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM ejecuciones_ssor WHERE id = %s
        ''', (id_ejecucion,))
        
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return resultado
