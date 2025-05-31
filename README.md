# 📦 Sistema de Gestión de Servicios y Clientes

Este proyecto consiste en un sistema basado en consola, desarrollado en **Python**, para la administración de clientes, servicios, ventas y gestión de datos en general. Toda la información se guarda de forma persistente en un archivo `JSON`.

---

## 📚 Descripción General

Este sistema está dividido en los siguientes módulos principales:

### 1. 🧑‍💼 Módulo Administrador
- Visualizar todos los clientes registrados.
- Registrar nuevos clientes.
- Eliminar clientes.
- Actualizar datos de contacto, dirección o nombre.

### 2. 🛠️ Gestión de Servicios
- Ver todos los servicios disponibles.
- Crear un nuevo servicio.
- Eliminar servicios existentes.
- Modificar nombre, descripción o precio de un servicio.

### 3. 📊 Reportes
- *(En desarrollo)*

### 4. 💰 Realizar Ventas
- Elegir un cliente y asignarle uno o varios servicios comprados.
- Registra los servicios usados en el historial del cliente.

### 5. 🎁 Bonificaciones para Clientes Leales
- *(En desarrollo)*

---

## 🧪 Tecnologías Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-5E5C5C?style=for-the-badge&logo=json&logoColor=white)

---

## 🗃️ Estructura del Proyecto

- `main.py`: Código principal del sistema. Contiene el menú y toda la lógica.
- `Datos.json`: Archivo que almacena de manera persistente los clientes y servicios.

### Formato del JSON

```json
[
  {
    "Tipo": "Usuarios",
    "Usuarios": [
      {
        "Nombre": "Brayan Stiven Maldonado Ortega",
        "Direccion": "cll 1c 5b - 45",
        "InfoContacto": "3103903374",
        "Categoria": "Cliente Nuevo",
        "ServiciosUsados": []
      }
    ]
  },
  {
    "Tipo": "Servicios",
    "Servicios": [
      {
        "Servicio": [
          {
            "Nombre": "Fibra optica",
            "Descripcion": "Servicio de Fibra optica",
            "Precio": 80000
          }
        ]
      }
    ]
  }
]
```

## ▶️ Instrucciones de Uso

- Clona el repositorio o descarga los archivos `main.py` y `Datos.json`.

- Abre el proyecto en Visual Studio Code o cualquier editor Python.

- Asegúrate de tener instalado Python 3.

- Ejecuta el programa:

```bash
python main.py
```

## 💡Características Destacadas

- Interfaz basada en consola intuitiva.

- Menú principal con navegación por números.

- Almacenamiento persistente con archivos .json.

- Validación de entradas con try/except.

- Código modular y fácil de extender.

---

👨‍💻 Desarrollado por
Brayan Stiven Maldonado Ortega
Estudiante de Campuslands
TI: 1.090.404.470
