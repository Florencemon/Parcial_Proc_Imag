from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import argparse


class ProcesadorDeImagenes:
    '''
    Clase para alojar las funciones de procesamiento de imágenes.
    '''

    # Constructor
    def __init__(self, ruta_imagen: str):
        '''
        Constructor de la clase, carga la imagen indicada.

        Parámetros:
            ruta_imagen (str): ruta al archivo de imagen a usar como base. 
        '''

        self.imagen = Image.open(ruta_imagen)

        print(f"Imagen cargada correctamente")


    def guardar_imagen(self, imagen, nombre_archivo):
        '''
        Método para guardar la imagen.

        Parámetros:
            imagen (PIL.Image.Image): imagen a guardar en disco
            nombre_archivo (str): nombre del archivo de salida
        '''
        imagen.save(nombre_archivo)

        print(f"Imagen guardada correctamente como {nombre_archivo}")

    #creamos la funcion gaussiano
    def gaussiano(self, desenfoque: float):   
        """
        Aplica un desenfoque gaussiano sobre la imagen para suavizar detalles y reducir variaciones bruscas.

        Args:
            desenfoque:
                Intensidad del desenfoque gaussiano.

        Returns:
            Imagen con el filtro de desenfoque aplicado.

        Observaciones:
            - El radio utilizado se limita entre 0 y 20.
            - Valores altos generan una imagen más suavizada.
            - A partir de ciertos niveles puede perderse demasiado detalle visual.

        Referencia:
            https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
        """
        if desenfoque > 0 and desenfoque < 20:
            gaussian_blur = self.imagen.filter(ImageFilter.GaussianBlur(radius=desenfoque))
            self.guardar_imagen(gaussian_blur, "imagenes/mabel_gaussblur.jpg")
        else:
            print(f"El número {desenfoque} no está entre los parámetros aceptados en la función")


    def brillo(self, nivel: float):
        """
        Ajusta el brillo de una imagen utilizando el módulo ImageEnhance de Pillow.

        Args:
            imagen:
                Imagen PIL sobre la que se aplicará el ajuste de brillo.

            factor:
                Valor numérico que controla la intensidad del brillo.
                
                - Valores cercanos a 0 producen una imagen más oscura.
                - El valor 1 mantiene la imagen original.
                - Valores mayores a 1 aumentan el brillo.

        Returns:
            Imagen PIL con el brillo modificado.

        Observaciones:
            - Hasta valores cercanos a 1.8 el resultado suele verse natural.
            - Valores altos, como 5 o superiores, pueden saturar la imagen
            y generar grandes zonas blancas.

        Referencia:
            https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html#PIL.ImageEnhance.Brightness
        """
        enhancer = ImageEnhance.Brightness(self.imagen)

        if nivel >= 0 and nivel <= 5:
            img_procesada = enhancer.enhance(nivel) # Aplica o elimina brillo según lo enviado por parámetro
            self.guardar_imagen(img_procesada, "imagenes/mabel_brightness.jpg")
        else:
            print(f"El número {nivel} no está entre los parámetros aceptados en la función")

    def rotacion(self, giro):
        '''

        '''
        if giro >= 0 and giro <= 360:
            rotar = self.imagen.rotate(giro)
            self.guardar_imagen(rotar, "imagenes/mabel_rotada.jpg")
        else:
            print(f"El número {giro} no está entre los parámetros aceptados en la función")
        

# -------------------------
# ARGPARSE
# -------------------------

parser = argparse.ArgumentParser(
    description="Procesador de imágenes con Pillow"
)

# parámetro obligatorio
parser.add_argument(
    "imagen",
    help="Ruta de la imagen a procesar"
)

# parámetro opcional
parser.add_argument(
    "--gauss",
    type=float,
    default=2,
    help="Nivel de desenfoque gaussiano"
)

# parámetro opcional
parser.add_argument(
    "--brillo",
    type=float,
    default=1,
    help="Nivel de brillo"
)

# parámetro opcional
parser.add_argument(
    "--rotar",
    type=float,
    default=0,
    help="Ángulo de rotación"
)

args = parser.parse_args()

''' 
ejecucion CLI
'''

procesador = ProcesadorDeImagenes(args.imagen)

procesador.gaussiano(args.gauss)

procesador.brillo(args.brillo)

procesador.rotacion(args.rotar)

'''
parser = argparse.ArgumentParser(description="Aplicar filtro gaussiano")

# obligatorio
parser.add_argument(
    "imagen",
    help="Ruta de la imagen a procesar"
)

# opcional
parser.add_argument(
    "--radio",
    type=int,
    default=2,
    help="Nivel de desenfoque gaussiano (default: 2)"
)

args = parser.parse_args()

print("Imagen:", args.imagen)
print("Radio:", args.radio)

'''