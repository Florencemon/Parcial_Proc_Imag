from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import argparse


class ProcesadorDeImagenes:
    '''
    Clase para alojar las funciones de procesamiento de imágenes.
    ***************
    DEBATE GRUPAL: tuvimos el debate sobre si debería la clase recibir la imagen directamente o solo la ruta y después de terminar el código decidimos que lo merjor era la ruta porque es mas intuitivo para CLI.
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
		
	*************
	DEBATE GRUPAL:  debatimos si guardar debería ser parte de cada método o centralizado desde acá. por votacion fuimos por la centralización para evitar repetir código, aunque una integrante propuso retornar la imagen y ddejar el guardado a quien usa el metodo.

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

        ***************
        DEBATE GRUPAL:  
        Revisamos la documentacion para saber cuál era el tope admitido por la funcion gauss de la libreria pillow y nos dice que prácticamente no hay tope, pero fuimos probando y hasta nivel 20 se permite un suavizado en el que todavía se pueda distinguir la imagen.
        """
        if desenfoque > 0 and desenfoque < 20:
            gaussian_blur = self.imagen.filter(ImageFilter.GaussianBlur(radius=desenfoque))
            self.guardar_imagen(gaussian_blur, "imagenes/mabel_gaussblur.jpg")
        else:
            print(f"El número {desenfoque} no está entre los parámetros aceptados en la función")


    def brillo(self, nivel: float):
        '''
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

        ***************
        DEBATE GRUPAL: 
        en brillo estuvimos a punto de usar 2.0 como tope max. pero una integrante mostró un caso donde 3.5 se veía relativamente natural, pero que 5.0 o superior dejaba muchas zonas blancas y cualquier valor superior aunque técnicamente funciona, casi toda la imagen termina saturada (y lo vimos en la documentacion de brightness). pusimos ese valor como tope pero sabemos que lo correcto es solo advertir en vez de bloquear.
        '''
        enhancer = ImageEnhance.Brightness(self.imagen)

        if nivel >= 0 and nivel <= 5:
            img_procesada = enhancer.enhance(nivel) # Aplica o elimina brillo según lo enviado por parámetro
            self.guardar_imagen(img_procesada, "imagenes/mabel_brightness.jpg")
        else:
            print(f"El número {nivel} no está entre los parámetros aceptados en la función")

    def rotacion(self, giro):
        '''
        Rota la imagen el número de grados indicado en sentido antihorario.

        Args:
            giro:
                Ángulo de rotación en grados.

                - 0 mantiene la imagen original.
                - 90, 180, 270 son las rotaciones más comunes.
                - Valores intermedios (ej. 45°) pueden generar esquinas
                recortadas, ya que Pillow no expande el lienzo por defecto.

        Returns:
            Imagen rotada guardada en disco.

        Observaciones:
            - El rango aceptado es de 0 a 360 grados.
            - La rotación es en sentido antihorario (comportamiento por
            defecto de Pillow).
            - Si se necesitara sentido horario, habría que pasar (360 - giro)
            o usar valores negativos, lo cual actualmente el validador no permite.

        Referencia:
            https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate


        ***************
        DEBATE GRUPAL: 
        estuvimos buscando en la documentacion porqué Pillow no agranda el lienzo para acomodar la imagen rotada, lo que hace es recortar las esquinas y por eso decidimos dejarlo documentado. 
        también buscamos si el tope era 360 o -360 y la realidad es que se puede girar por cualquier número, pero si supera los 360 grados, vuelve a girar, así que no es relevante el tope. Además buscamos y se puede girar en sentido negativo

        '''
        if giro >= 0 and giro <= 360:
            rotar = self.imagen.rotate(giro)
            self.guardar_imagen(rotar, "imagenes/mabel_rotada.jpg")
        else:
            print(f"El número {giro} no está entre los parámetros aceptados en la función")
        

# ***************
# ARGPARSE

'''
los defaults (gauss=2, brillo=1, rotar=0) son conservadores de niveles: si el usuario no especifica valores, la imagen sale igual.
'''

parser = argparse.ArgumentParser(
    description="Procesador de imágenes con Pillow"
)

# parámetro obligatorio
parser.add_argument(
    "imagen",
    help="Ruta de la imagen a procesar"
)

# parametro para desenfoque gaussiano (es opcional para CLI) y se usa colocando por ejemplo, --gauss 5 
parser.add_argument(
    "--gauss",
    type=float,
    default=2,
    help="Nivel de desenfoque gaussiano"
)

# parametro para nivel de brillo (es opcional para CLI) y se usa colocando por ejemplo, --brillo 1.5 
parser.add_argument(
    "--brillo",
    type=float,
    default=1,
    help="Nivel de brillo"
)

# parametro para angulo de rotación (es opcional para CLI) y se usa colocando por ejemplo, --rotar 90 

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
*********** *
esta fue la versión anterior del parser antes de unificarlo en la clase pero se dejo comentado por si se necesita volver a un enfoque simple de un solo filtro por ejecución.
con esto quisimos demostrar como estaba, pero sabemos que lo correcto es borrar en la limpieza de codigo.

parser = argparse.ArgumentParser(description="Aplicar filtro gaussiano")

# obligatorio
parser.add_argument(
    "imagen",
    help="Ruta de la imagen a procesar"
)

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
