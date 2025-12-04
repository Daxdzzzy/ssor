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

![Interfaz principal de la pagina web](./Pantallazos/interfaz.png)

_Agrega aquí las capturas de pantalla del sistema cuando estén disponibles._

---

graph TB
    Root[📁 Proyecto SSOR]
    
    Root --> Main[main.py]
    Root --> README[README.md]
    Root --> Pantallazos[📁 Pantallazos]
    
    Root --> Control[📁 capaControl]
    Root --> Interfaz[📁 capaInterfaz]
    Root --> Metodo[📁 capaMetodo]
    Root --> Servicios[📁 capaServicios]
    Root --> Traduccion[📁 capaTraduccion]
    
    Control --> CF[control_de_flujo.py]
    
    Interfaz --> Servidor[servidor.py]
    Interfaz --> Static[📁 static]
    Interfaz --> Templates[📁 templates]
    
    Static --> CSS[📁 css]
    Static --> JS[📁 js]
    CSS --> StylesCSS[styles.css]
    JS --> ScriptJS[script.js]
    Templates --> Index[index.html]
    
    Metodo --> SSOR[ssor.py]
    Metodo --> Valid[validaciones.py]
    
    Servicios --> InitBD[inicializar_bd.py]
    Servicios --> ServBD[servicio_bd.py]
    Servicios --> ServGraf[servicio_graficas.py]
    Servicios --> Graficas[📁 graficas]
    
    Traduccion --> Parse[parseador_ecuaciones.py]
    
    Pantallazos --> InterfazPNG[interfaz.png]
    
    style Root fill:#2c3e50,stroke:#34495e,color:#ecf0f1
    style Control fill:#3498db,stroke:#2980b9,color:#fff
    style Interfaz fill:#3498db,stroke:#2980b9,color:#fff
    style Metodo fill:#3498db,stroke:#2980b9,color:#fff
    style Servicios fill:#3498db,stroke:#2980b9,color:#fff
    style Traduccion fill:#3498db,stroke:#2980b9,color:#fff
    style Static fill:#95a5a6,stroke:#7f8c8d,color:#fff
    style Templates fill:#95a5a6,stroke:#7f8c8d,color:#fff
    style CSS fill:#95a5a6,stroke:#7f8c8d,color:#fff
    style JS fill:#95a5a6,stroke:#7f8c8d,color:#fff
    style Graficas fill:#95a5a6,stroke:#7f8c8d,color:#fff
    style Pantallazos fill:#95a5a6,stroke:#7f8c8d,color:#fff
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
