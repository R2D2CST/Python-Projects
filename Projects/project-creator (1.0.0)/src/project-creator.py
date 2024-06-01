# Librerías nativas de Python.
from tkinter import filedialog
import os
# Librerías de terceros.
from tqdm import tqdm

def crear_ruta (path:str, folder:str) -> None:
    """
    Este procedimiento recibe una ruta (path) y una cadena de texto, las une creando una nueva
    ruta donde se crea el proyecto con su arquitectura.
    Args:
        path (str): ruta en el sistema donde se localiza el proyecto.
        folder (str): cadena de texto de la ruta relativa del proyecto y su arquitectura.
    """
    # Utilizamos la ruta absoluta al directorio del script para construir la ruta completa
    full_path = os.path.join(path, folder)
    if not os.path.exists (full_path):
        os.makedirs (full_path)
    pass

# Colocamos el Header de la aplicación.
print ("______________________________________________________________________________________")
print ("|  Bienvenido a la automatización creación de proyectos de programación [1.0.0]      |")
print ("|  Elaborado por José Arturo Castella Lasaga                                         |")
print ("|  Contacto:                                                                         |")
print ("|  qfbarturocastella@gmail.com                                                       |")
print ("______________________________________________________________________________________")
while True:
    print ("\nMenu Principal:")
    print ("1.- Salir del Programa.")
    print ("2.- Crear un proyecto Monolítico.")
    print ("3.- Crear un proyecto Micro Servicios.")
    print ("4.- Crear un proyecto por Capas.")
    print ("5.- Acerca de los tipos de proyectos.")
    selection = input ("Por favor ingresa la opción seleccionada: ")
    try:
        selection = int (selection)
    except ValueError:
        print ("Por favor ingresa solamente el número de opción deseada.")
        continue
    if selection == 1:
        break
    if selection == 5:
        mensaje = """
            Proyectos Monolíticos:
            + Fácil de desarrollar y desplegar.
            + Menos compleja en términos de configuración y gestión.
            + Buena opción para aplicaciones pequeñas y medianas.
            - Dificultad para escalar horizontalmente.
            - Mayor riesgo de fallos y errores.
            - Acoplamiento fuerte entre los componentes.
            ////Ejemplo de arquitectura:
            |------Proyecto
            |----src
            |----app
            Proyectos por Micro Servicios:
            + Escalabilidad y flexibilidad mejoradas.
            + Facilita la implementación continua y la entrega rápida.
            + Mayor resiliencia frente a fallos.
            - Mayor complejidad en el desarrollo y mantenimiento.
            - Gestión de la comunicación entre servicios.
            - Posible sobrecarga de red.
            ////Ejemplo de arquitectura:
            |------Proyecto
            |----app
            |----servicio 1
            |--src
            |--lib
            |----servicio 2
            |--src
            |--lib
            Proyectos por Capas
            + Separación clara de responsabilidades.
            + Facilita el reuso y la modularidad del código.
            + Mayor mantenibilidad y escalabilidad.
            - Puede haber una sobrecarga de abstracción.
            - Comunicación entre capas puede ser costosa.
            - Requiere una planificación y diseño cuidadoso.
            ////Ejemplo de arquitectura:
            |------Proyecto
            |----app
            |----db
            |----docs
            |----test
            |----src
            |--lib
            |--gui
        """
        print (mensaje)
        input ("\nPulsa Enter para Regresar el menu principal.")
    if selection !=5:
        print ("Por favor ingresa el nombre de tu proyecto y pulsa enter")
        project_name:str = input (":")
        print ("Por favor selecciona una ruta donde crear el proyecto.")
        project_path:str = ""
        while project_path == "":
            project_path:str = filedialog.askdirectory ()
            if project_path == "":
                print ("Se ha cancelado la selección de ruta, reiniciando...")
                break
        if project_path == "":
            continue
    if selection == 2:
        total_interactions = 100
        progress_bar = tqdm(
            total=total_interactions,
            desc="Procesando",
            unit="instrucciones",
            bar_format="{desc}: {percentage:3.0f}%|{bar:30}{r_bar}",
            colour='green'
        )
        # Creamos la ruta del proyecto. 
        crear_ruta (project_path, f"{project_name}")
        progress_bar.update (33)
        # Creamos las carpetas del proyecto Monolítico.
        crear_ruta (project_path, f"{project_name}/src")
        progress_bar.update (33)
        crear_ruta (project_path, f"{project_name}/app")
        progress_bar.update (34)
        progress_bar.close ()
        continue
    if selection == 3:
        micro_services:list[str] = []
        while True:
            print ("Por favor ingresa el número de microservicios a conetener el proyecto:")
            no_microservicios = input ()
            try:
                no_microservicios = int(no_microservicios)
                break
            except ValueError:
                print ("Por favor ingresa un numero entero.")
                continue
        total_interactions = no_microservicios
        progress_bar = tqdm(
            total=total_interactions,
            desc="Procesando",
            unit="instrucciones",
            bar_format="{desc}: {percentage:3.0f}%|{bar:30}{r_bar}",
            colour='green'
        )
        for i in range (no_microservicios):
            micro = input (f"Por favor ingresa el micro servicio {i} de {no_microservicios}: ")
            micro_services.append (micro)
        # Creamos la ruta del proyecto.
        crear_ruta (project_path, f"{project_name}")
        crear_ruta (project_path, f"{project_name}/app")
        # Creamos la ruta de cada microservicio.
        for i in range (no_microservicios):
            crear_ruta (project_path, f"{project_name}/{micro_services [i]}")
            crear_ruta (project_path, f"{project_name}/{micro_services [i]}/src")
            crear_ruta (project_path, f"{project_name}/{micro_services [i]}/lib")
            progress_bar.update (1)
        progress_bar.close ()
        continue
    if selection == 4:
        total_interactions = 100
        progress_bar = tqdm(
            total=total_interactions,
            desc="Procesando",
            unit="instrucciones",
            bar_format="{desc}: {percentage:3.0f}%|{bar:30}{r_bar}",
            colour='green'
        )
        # Creamos la ruta del proyecto. 
        crear_ruta (project_path, f"{project_name}")
        progress_bar.update (100//8)
        # Creamos las carpetas del proyecto por Capas.
        crear_ruta (project_path, f"{project_name}/src")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/src/lib")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/docs")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/db")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/src/gui")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/app")
        progress_bar.update (100//8)
        crear_ruta (project_path, f"{project_name}/test")
        progress_bar.close()
        continue
    continue
print ("Pulsa enter para terminar.")
input ()