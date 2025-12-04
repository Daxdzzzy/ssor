#!/usr/bin/env python3
"""
Script para inicializar la base de datos PostgreSQL
Ejecutar SOLO UNA VEZ antes de usar el sistema
"""

import sys
sys.path.append('/home/ZzzZzz/AlgoritmosNumericosParaIngenieria/proyectoSSOR')

from capaServicios.servicio_bd import ServicioBD

if __name__ == "__main__":
    print("Inicializando base de datos PostgreSQL...")
    
    servicio = ServicioBD()
    
    # Crear base de datos
    servicio.crear_base_datos()
    
    # Crear tablas
    servicio.crear_tablas()
    
    print("\n✓ Base de datos inicializada correctamente")
    print("  - Base de datos: ssor_db")
    print("  - Tabla: ejecuciones_ssor")
    print("\nYa puedes usar el sistema normalmente.")
