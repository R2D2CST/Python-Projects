# Librerías nativas de Python.
import sys, os
# Importamos sys para gestionar el sistema y os para interactuar con el SO.
# Librerías de terceros.
import openpyxl # Importamos openpyxl para el manejo de archivos del tipo Excel.
from docx import Document
from docxtpl import DocxTemplate # Importamos docxtpl para poder manejar los archivos de tipo Word.
from tqdm import tqdm
# Librerías propias.

# Colocamos el Header de la aplicación.
print ("____________________________________________________________________________")
print ("|  Bienvenido a la automatización de plantillas en su versión [1.1.0]      |")
print ("|  Elaborado por José Arturo Castella Lasaga                               |")
print ("|  Contacto:                                                               |")
print ("|  qfbarturocastella@gmail.com                                             |")
print ("____________________________________________________________________________")

# Obtenemos la ruta absoluta al directorio donde se encuentra el ejecutable o el script
if getattr(sys, 'frozen', False):
    # Ruta absoluta al directorio del ejecutable en el entorno empaquetado
    script_directory = os.path.dirname(sys.executable)
else:
    # Ruta absoluta al directorio del script en el entorno no empaquetado
    script_directory = os.path.dirname(os.path.abspath(__file__))

# Aquí definimos las funciones que usaremos dentro de nuestro bucle del programa.
def verificar_ruta (path:str) -> None:
    """
    Este procedimiento recibe una ruta (path) y verifica si existe, caso contrario crea la ruta.
    Args:
        path (str): ruta a verificar como una cadena de texto.
    """
    # Utilizamos la ruta absoluta al directorio del script para construir la ruta completa
    full_path = os.path.join(script_directory, path)
    if not os.path.exists (full_path): # Verifica existe la ruta proporcionada.
        os.makedirs (full_path)        # Crea la ruta si no existe.
    pass

def crear_database ()->None:
    """
    Este procedimiento crea libreo de excel que sostendrá la base de datos en la hoja panel.
    Args: None
    """
    # Creamos la ruta donde se guarda el archivo de Excel.
    excel_file_path = os.path.join(script_directory, "data_base.xlsx")
    # Creamos el archivo de Excel.
    workbook = openpyxl.Workbook ()
    # Creamos la Hoja del archivo como panel.
    panel_sheet = workbook.create_sheet ("panel")
    # Registro de datos en las celdas.
    panel_sheet['A1'] = "Titulo de Columna"
    panel_sheet['A2'] = "palabra_clave"
    panel_sheet['A3'] = "Corrida 1"
    panel_sheet['A4'] = "Corrida 2"
    panel_sheet['A5'] = "Corrida 3"
    panel_sheet['B1'] = "Titulo de Columna2"
    panel_sheet['B2'] = "palabra_clave2"
    panel_sheet['B3'] = "Valor 1"
    panel_sheet['B4'] = "Valor 2"
    panel_sheet['B5'] = "Valor 3"
    panel_sheet['C1'] = "Titulo de Columna3"
    panel_sheet['C2'] = "palabra_clave3"
    panel_sheet['C3'] = "Valor 1"
    panel_sheet['C4'] = "Valor 2"
    panel_sheet['C5'] = "Valor 3"
    # Eliminar la hoja por defecto (Sheet) si existe
    try:
        default_sheet = workbook["Sheet"]
        workbook.remove(default_sheet)
    except Exception as e:
        print (f"Error presentado al crear el archivo de Excel: {e}")
    # Guardamos el archivo de Excel.
    workbook.save (excel_file_path)
    pass

def crear_plantilla ()-> None:
    """
    Procedimiento crea un archivo de Word con las instrucciones para crear plantillas a
    automatizar con la base de datos en Excel.
    Args: None
    """
    # Construir la ruta del archivo de Word
    word_file_path = os.path.join(script_directory, "Templates", "template.docx")
    # Crear un nuevo documento de Word
    doc = Document()
    # Agregar el contenido al documento
    content = """
    Bienvenido, este es un ejemplo de plantilla para automatizar tus reportes o informes
    usando palabras clave como en el siguiente ejemplo: {{palabra_clave}}.
    Podrás reemplazar estas palabras clave vaciando el contenido dentro de la base de datos.

    En el documento de Excel debes llenar la Base de datos (database.xlsx) en la fila 1 con
    los títulos de las columnas, estos no se vaciarán en las plantillas. a partir de la fila
    2 el programa va a leer todas las celdas como palabras clave. Aquí deberás registrarlas
    sin los dobles corchetes (Importante que no tengan los dobles corchetes).

    Siéntete libre de correr el programa con la plantilla y la base de datos para ver como
    funciona el sistema.

    Ejemplo para la palabra clave -> palabra_clave
    
    Debajo de estas palabras calves el programa va a leer cada renglón como el valor asociado
    a esta palabra clave. Importante la Columna A será la única que además de funcionar de
    esta forma también le da valor a cada carpeta (corrida) del programa como reportes
    generados.
    
    palabra clave   : {{palabra_clave}}
    palabra clave 2 : {{palabra_clave2}}
    palabra clave 3 : {{palabra_clave3}}
    """
    doc.add_paragraph(content)
    # Guardar el documento en la carpeta Templates
    doc.save(word_file_path)
    pass

def template_paths () -> None:
    """
    Obtiene una lista de rutas de plantillas en el directorio "Templates".
    Returns:
        list[str]: Lista de rutas de plantillas.
    """
    # Construir la ruta del directorio de plantillas
    templates_directory = os.path.join(script_directory, "Templates")
    # Obtener las rutas absolutas de todas las plantillas en el directorio "Templates"
    return [os.path.join(templates_directory, file) for file in os.listdir(templates_directory)]

def renderizar_plantilla (path_plantilla:str, salida_plantilla:str, contexto:dict)-> None:
    """
    Renderiza una plantilla de documento Word con el contexto dado y la guarda en el
    directorio de salida.
    Args:
        path_plantilla (str): Ruta de la plantilla.
        salida_plantilla (str): Ruta de salida del documento renderizado.
        contexto (dict): Contexto con los datos para renderizar la plantilla.
    """
    # Cargar la plantilla
    document = DocxTemplate(path_plantilla)
    # Renderizar el documento con el contexto dado
    document.render(contexto)
    # Guardar el documento renderizado en la ruta especificada
    document.save(salida_plantilla)
    pass

# Iniciamos nuestro bucle de la aplicación.
while True:
    print ("Opciones del sistema:")
    print ("1.- Salir del sistema.")
    print ("2.- Primera vez en el sistema (Crear Base de Datos y Ejemplo de Plantilla).")
    print ("3.- Renderizar las plantillas con eel contenido de la Base de Datos.")
    try:
        selection : (int) = int (input ("Ingrese el número de la opción deseada: "))
    except ValueError:
        print ("Por favor ingrese solamente el número.")
        continue
    if selection == 1:
        break
    if selection == 2:
        total_interactions = 100
        progress_bar = tqdm(
            total=total_interactions,
            desc="Procesando",
            unit="instrucciones",
            bar_format="{desc}: {percentage:3.0f}%|{bar:30}{r_bar}",
            colour='green'
        )
        verificar_ruta ("Templates")
        progress_bar.update (33)
        crear_database ()
        progress_bar.update (33)
        crear_plantilla ()
        progress_bar.update (34)
        progress_bar.close ()
        print ("\nSe ha creado exitosamente la base de datos 'data_base.xlsx' asi como")
        print ("la carpeta Templates. Donde se contiene un ejemplo de plantilla para")
        print ("renderizar la base de datos.")
        input ("\nPulsa enter para regresar al menu principal.")
        continue
    if selection == 3:
        # Verificamos exista una carpeta llamada Rendered_Templetes donde depositar los documentos.
        verificar_ruta ("Rendered_Templates")
        # Abrir el archivo de Excel y obtener la hoja de cálculo
        workbook = openpyxl.load_workbook("data_base.xlsx")
        panel_ws = workbook["panel"]
        # Creamos un total de corridas para calcular el progreso en la barra de progreso.
        total_corridas = len(list(panel_ws.iter_rows(min_row=3)))
        total_documentos_por_corrida = len(template_paths())
        total_documentos = total_corridas * total_documentos_por_corrida
        # Creamos una barra de progreso.
        progress_bar = tqdm(
            total= total_documentos,
            desc="Procesando",
            unit="documentos",
            bar_format="{desc}: {percentage:3.0f}%|{bar:30}{r_bar}",
            colour='green'
        )
        # Extraer las llaves de la fila 2 (Omitiendo los encabezados de las columnas)
        keys = [cell.value for cell in panel_ws[2]]
        # Iterar sobre cada fila de la hoja de cálculo y generar informes
        for row in panel_ws.iter_rows(min_row=3, values_only=True):
            # Crear el diccionario de contexto para esta fila
            contexto = {keys[i]: value for i, value in enumerate(row)}            
            # Crear la carpeta para el informe si no existe
            verificar_ruta(f"Rendered_Templates\{str(contexto[keys[0]])}")
            # Iterar sobre cada plantilla y renderizarla
            for path_plantilla in template_paths():
                # Construir la ruta de salida del documento renderizado
                salida_plantilla = os.path.join(
                    script_directory,
                    "Rendered_Templates",
                    str(contexto[keys[0]]),
                    f"rendered_{os.path.basename(path_plantilla)}"
                )
                # Renderizar la plantilla y guardar el documento renderizado
                renderizar_plantilla(path_plantilla, salida_plantilla, contexto)
                progress_bar.update(1)
        progress_bar.close ()
        print ("\nLas plantillas se han renderizado conforme al contenido en la base de datos.")
        input ("\nPulsa enter para regresar al menu principal.")
        continue
input ("\nHasta luego, presiona enter para cerrar la terminal.")