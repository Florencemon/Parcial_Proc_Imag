# PROCESADOR DE IMÁGENES — PARCIAL

## Integrantes

- Castelao Bravo
- Cappato Carolina
- Chirino Florencia

---

## Descripción

Este proyecto consiste en una aplicación desarrollada en Python para realizar procesamiento digital de imágenes utilizando la biblioteca Pillow.

El objetivo principal fue implementar distintas técnicas básicas de procesamiento de imágenes, permitiendo modificar fotografías mediante parámetros ingresados desde la terminal.

Entre las operaciones implementadas se encuentran:

- desenfoque gaussiano;
- ajuste de brillo;
- rotación de imágenes.

Además, se utilizó el módulo `argparse` para gestionar argumentos desde línea de comandos y facilitar la configuración de los parámetros de procesamiento.

Inicialmente se intentó incorporar OpenCV, pero debido a inconvenientes de configuración y compatibilidad en el entorno de trabajo, se optó por continuar el desarrollo utilizando únicamente Pillow.

---

## Tecnologías utilizadas

- Python 3
- Pillow
- argparse

---

## Instalación

Instalar las dependencias necesarias:

```bash
pip install pillow
```

---

## Ejecución

### Ejemplo básico

```bash
python programa.py imagenes/mabel.jpg
```

### Ejemplo con parámetros

```bash
python programa.py imagenes/mabel.jpg --gauss 5 --brillo 1.5 --rotar 90
```

---

## Parámetros disponibles

| Parámetro | Descripción |
|---|---|
| imagen | Ruta de la imagen a procesar |
| --gauss | Nivel de desenfoque gaussiano |
| --brillo | Intensidad del brillo |
| --rotar | Ángulo de rotación de la imagen |

---

## Técnicas implementadas

### Desenfoque gaussiano

Aplica un suavizado sobre la imagen mediante un filtro gaussiano, reduciendo detalles y transiciones bruscas entre píxeles.

### Ajuste de brillo

Permite aumentar o disminuir la luminosidad de la imagen según el factor ingresado.

### Rotación de imágenes

Realiza la rotación de la imagen utilizando el ángulo especificado por el usuario.

---

## Resultados generados

El programa guarda automáticamente las imágenes procesadas en archivos independientes.

Ejemplos:

```text
mabel_gaussblur.jpg
mabel_brightness.jpg
mabel_rotada.jpg
```

---

## Estructura general del proyecto

```text
├── programa.py
├── imagenes/
│   └── mabel.jpg
└── resultados/
```

---

## Referencias y documentación

- https://pillow.readthedocs.io/en/stable/
- https://docs.python.org/3/library/argparse.html
- https://www.python.org/doc/
