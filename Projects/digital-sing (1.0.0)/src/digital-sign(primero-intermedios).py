# Importamos las librerías nativas de Python.
import os
import re
import socket
from datetime import datetime
from tkinter import filedialog

# Importamos las librerías de terceros en Python.
from docx import Document
from docxtpl import DocxTemplate
from docx2pdf import convert

# Definimos las funciones que serán usadas en la aplicación.
def obtener_datos_firma()->tuple [str]:
    """
    La función obtiene los datos de la persona que firma el documento (nombre, rubrica, fecha y hora,
    id del equipo, dirección ip del equipo) y retorna los valores.
    Returns:
        nombre_persona (str): nombre de la persona que firma.
        rubrica_persona (str): rubrica de la persona que firma.
        fecha_hora (str): fecha y hora en la que se ejecuta la firma.
        id_equipo (str): id del equipo donde se firma.
        direccion_ip (str): ip del equipo donde se firma.
    """
    while True:
        nombre_persona = input("Ingrese su nombre: ")
        if nombre_persona == "":
            print ("Por favor ingrese su nombre.")
        else:
            break
    while True:
        rubrica_persona = input("Ingrese su rubrica: ")
        if rubrica_persona == "":
            print ("Por favor ingrese su nombre.")
        else:
            break
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_equipo = os.environ.get('COMPUTERNAME')
    direccion_ip = socket.gethostbyname(socket.gethostname())
    return nombre_persona, rubrica_persona, fecha_hora, id_equipo, direccion_ip

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

def convertir_docx_a_pdf(archivo_docx, archivo_pdf):
    """
    Convierte un archivo .docx a un archivo .pdf.
    Args:
    - archivo_docx (str): Ruta del archivo .docx a convertir.
    - archivo_pdf (str): Ruta del archivo .pdf de salida.
    """
    # Convertir el archivo a PDF
    convert(archivo_docx, archivo_pdf)
    # Eliminar el archivo temporal
    os.remove(archivo_docx)
    pass

def firmar_documento(nombre_archivo_pdf: str) -> None:
    """
    El procedimiento recibe la ruta del archivo PDF y retorna el documento firmado.
    Args:
        nombre_archivo_pdf (str): Ruta del archivo PDF como una cadena de texto.
    """
    # Obtenemos los datos de la firma del documento.
    nombre_persona, rubrica_persona, fecha_hora, id_equipo, direccion_ip = obtener_datos_firma ()
    # Creamos el contexto.
    contexto = {
        "sitio_de_firma" : f"{nombre_persona}\n{rubrica_persona}\n{fecha_hora}\n{id_equipo}\n{direccion_ip}"
    }
    # Creamos la ruta de salida.
    nombre_archivo_firmado = f"{os.path.splitext(nombre_archivo_pdf)[0]}_firmado.docx"
    # Renderizamos el documento.
    renderizar_plantilla (nombre_archivo_pdf, nombre_archivo_firmado, contexto)
    nombre_archivo_pdf_firmado = f"{os.path.splitext(nombre_archivo_pdf)[0]}_firmado.pdf"
    pass


print ("_________________________________________________________________________________________")
print ("| Bienvenido a la firma digital de Documentos PDF para Laboratorios Cosmedilab SA. de CV.|")
print ("| Versión 1.0.0 desarrollado por L.Cortez                                                |")
print ("_________________________________________________________________________________________")
while True:
    terminos_condiciones = """
        El presente programa esta desarrollado para Laboratorios Cosmedilab S.A de C.V.
        La reproducción parcial o total de este sistema computacional queda totalmente
        prohibida sin la autorización escrita por parte de Laboratorios Cosmedilab.
        El presente sistema computacional tiene por objetivo el registro de firmas
        electrónicas en cumplimiento con la NOM-241-SSA1-2021 y CFR 21 parte 11.
        """
    print (terminos_condiciones)
    if input ("\nAcepta los términos y condiciones de uso.\nY para Si\nN para no\n(Y/N): ") in ["y", "si", "Y", "Si"]:
        break
    else:
        exit ()
while True:
    print ("Por favor selecione el documento a firmar.")
    archivo_path = filedialog.askopenfilename ()
    if archivo_path == "":
        print ("Se ha cancelado la selección, desea terminar el programa?")
        terminar = input ("Desea terminar el programa (Y/N): ")
        if terminar in ["y", "Y", "Si", "si"]:
            break
    firmar_documento (archivo_path)
    if input ("Desea firmar otro documento? (Y continuar/ N terminar): ") in ["y", "Y", "Si", "si"]:
        continue
    break

# última linea de código.