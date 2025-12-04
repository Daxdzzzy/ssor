# Documentación Técnica

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Herramientas](#herramientas)
3. [Contribuciones](#contribuciones)
4. [Pantallazos](#pantallazos)
5. [Documentación](#documentación)
   - [Capa Control](#capa-control)
   - [Capa Interfaz](#capa-interfaz)
   - [Capa Método](#capa-método)
   - [Capa Traducción](#capa-traducción)
   - [Capa Servicios](#capa-servicios)

---

## Introducción

SSOR (Symmetric Successive Over-Relaxation) es un método iterativo utilizado para resolver sistemas de ecuaciones lineales de la forma:

**Ax = b**

### Requisitos del método
- La matriz **A debe ser simétrica**  
- Se recomienda que sea **diagonal dominante**  
- El parámetro de relajación **ω debe estar entre 0 y 2**

El método realiza **dos barridos por iteración**:
- Uno hacia adelante (SOR)
- Uno hacia atrás (SSOR)

Esto mejora notablemente la convergencia en comparación con métodos estándar.

---

## Herramientas

El proyecto utiliza las siguientes tecnologías:

- **Python (Flask)** – Backend y servicios.
- **HTML, CSS, JavaScript** – Interfaz de usuario.
- **PostgreSQL** – Base de datos relacional.

---

## Contribuciones

Las contribuciones al proyecto son bienvenidas.  
Para colaborar:

1. Hacer un *fork* del repositorio  
2. Crear una rama con la nueva funcionalidad  
3. Enviar un *pull request* con una descripción clara del aporte  

---

## Pantallazos

![Interfaz principal de la pagina web](/home/ZzzZzz/Pictures/screenshots/12-04-2025-124218.png)

_Agrega aquí las capturas de pantalla del sistema cuando estén disponibles._

---

## Documentación

Este proyecto está construido de manera modular, con las siguientes capas:

### Capa Control
Encargada de la comunicación entre la interfaz y la lógica del sistema. Gestiona peticiones y coordina el flujo de datos.

### Capa Interfaz
Contiene los componentes visuales desarrollados en HTML, CSS y JavaScript.

### Capa Método
Implementa el método SSOR y otros algoritmos numéricos necesarios.

### Capa Traducción
Convierte los datos de entrada en estructuras utilizables por el método y adapta los resultados para su presentación.

### Capa Servicios
Incluye la conexión con PostgreSQL, operaciones CRUD y servicios externos necesarios.

---

## Licencia
Este proyecto puede incluir una licencia abierta según preferencias del autor.
