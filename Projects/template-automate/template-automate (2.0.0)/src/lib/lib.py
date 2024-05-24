# We import native python libraries.
import sys, os
from tkinter import filedialog, messagebox
import shutil
"""
sys, os are libraries that we use to manage the operative system.
filedialog, messagebox are used to interact with the users selecting paths
and rasing messages with the user.
shutil is used for file moving proceses.
"""

# We import third party libraries.
import openpyxl
from docx import Document
"""
openpyxl is used for excel handling and data management in Excel.
Document form docx allow us to create the template  prototype.
"""

"""
This is my own libraries in python, designed for template-automate in it's
new version (2.0.0). This library has the objective to make a clearer code
and respect the main module only for execution.
"""

def library_path ()->str:
    """
    This function gets the path where the library program is been executed,
    this path will be an absolute path to the file in order to get files and
    saving elements. 
    """
    # We get the absolute path where the program will be executed.
    if getattr(sys, 'frozen', False):
        # If the program has been packed for distribution follows this path.
        script_directory = os.path.dirname(sys.executable)
    else:
        # If program is been executed as a python file.
        script_directory = os.path.dirname(os.path.abspath(__file__))
    return script_directory

def join_paths (script_directory:str, join_path:str)->str:
    """
    This function recibes the script directory and joins it with the second
    given path.
    Args:
        script_directory (str): first path where this program is been
        executed.
        join_path (str): second path where the joining element is located.
    """
    return os.path.join(script_directory, join_path)

def create_database ()->None:
    """
    This function is intended to build a complete Data Base Excel sheet as 
    data_base.xlsx containing the basic elements needed for the rendering 
    process.
    Args: None. 
    """
    # We ask the user the path where he wants to save the Excel document.
    project_path:str = ""
    project_path:str = filedialog.askdirectory ()
    if project_path == "":
        messagebox.showwarning ("Warning", "Data Base Creation Was Canceled")
        pass
    project_path = join_paths (project_path, "data_base.xlsx")

    # I create the workbook using the library openpyxl.
    workbook = openpyxl.Workbook ()
    panel_sheet = workbook.create_sheet ("panel")
    # Example Model
    panel_sheet['A1'] = "Column Title"
    panel_sheet['A2'] = "keyword"
    panel_sheet['A3'] = "Run 1"
    panel_sheet['A4'] = "Run 2"
    panel_sheet['A5'] = "Run 3"
    panel_sheet['B1'] = "Column Title2"
    panel_sheet['B2'] = "keyword2"
    panel_sheet['B3'] = "Value 1"
    panel_sheet['B4'] = "Value 2"
    panel_sheet['B5'] = "Value 3"
    panel_sheet['C1'] = "Column Title3"
    panel_sheet['C2'] = "keyword3"
    panel_sheet['C3'] = "Value 1"
    panel_sheet['C4'] = "Value 2"
    panel_sheet['C5'] = "Value 3"

    stats_sheet = workbook.create_sheet ("statistics")
    # Example Model
    stats_sheet["A1"] = "key words for a general-linear-regression"
    stats_sheet["A2"] = "x_mean"
    stats_sheet["A3"] = "y_mean"
    stats_sheet["A4"] = "sx_deviation"
    stats_sheet["A5"] = "sy_deviation"
    stats_sheet["A6"] = "r_coefficient"
    stats_sheet["A7"] = "a_origin"
    stats_sheet["A8"] = "b_slope"
    stats_sheet["A9"] = "n_size"
    stats_sheet["A10"] = "sum_xy"
    stats_sheet["A11"] = "sum_x_squared"
    stats_sheet["A12"] = "sum_y_squared"
    stats_sheet["A13"] = "p_value"
    stats_sheet["A14"] = "critical_value"
    stats_sheet["A15"] = "hypothesis_result"

    # Delete standard "Sheet"
    try:
        default_sheet = workbook["Sheet"]
        workbook.remove(default_sheet)
    except Exception as e:
        messagebox.showerror ("Error", f"Error presentado al crear el archivo de Excel: {e}")
    
    # We save the Excel file.
    workbook.save (project_path)
    pass

def create_template ()->None:
    """
    This procedure creates a Word document with instructions for creating templates to
    automate with the Excel database.
    Args: None
    """

    # We ask the user the path where he wants to save the Excel document.
    project_path:str = ""
    project_path:str = filedialog.askdirectory ()
    if project_path == "":
        messagebox.showwarning ("Warning", "Data Base Creation Was Canceled")
        pass
    project_path = join_paths (project_path, "template_model.docx")

    # Create a new Word document
    template_model = Document()

    # Add content to the document
    content = """
    Template Usage Instructions:

    Welcome!
    This document serves as an example template for automating your reports or documents using keywords.

    Using Keywords:
    You can replace the placeholders in double curly braces ({{keyword}}) with your desired content. These placeholders will be replaced with the corresponding data from your Excel database.

    Database Setup:

    In your Excel document (database.xlsx), start filling in the data from row 1 with your column titles. These titles will not be affected by the template.
    From row 2 onwards, enter your data. Each cell in these rows will be treated as a keyword for the template. Do not include the double curly braces when registering keywords.
    Program Execution:
    Feel free to run the program with both the template and the database to see how the system works.

    Example:
    For example, if you have a keyword "{{keyword}}" in your template, the program will replace it with the corresponding value from your database for each row.

    Important Note:
    Column A in your Excel database plays a special role. It not only functions as a keyword but also determines the folder structure for the generated reports. So, ensure that Column A contains unique identifiers for each report.

    Keywords and Corresponding Data:

    keyword : {{keyword}}
    keyword 2 : {{keyword2}}
    keyword 3 : {{keyword3}}
    Feel free to ask if you need further clarification or assistance!
    """
    template_model.add_paragraph(content)

    # Save the document in the Templates folder
    template_model.save(project_path)
    pass

def verify_path (path:str)->None:
    """
    This procedure takes in a path as argument, and if it does not exist it
    makes the path directory.
    Args:
        path (str): path to verify existence or build.
    """
    if not os.path.exists (path):
        os.makedirs (path)
    pass

def create_project_architecture (projects_paths:str, project_name:str)->None:
    """
    This procedure will create the Project Architecture branch tree for the
    application to store several projects at the same time.
    Args:
        project_name (str): takes in the project name as a string and with it
        builds up the branch tree.
    """
    project_specific_path = join_paths (projects_paths, project_name)
    verify_path (project_specific_path)
    templates_path = join_paths (project_specific_path, "Templates")
    database_path = join_paths (project_specific_path, "Data Base")
    verify_path (templates_path)
    verify_path (database_path)
    messagebox.showinfo ("Success", f"Project {project_name} added successfully.")
    pass

def file_path ()->str:
    """
    The current function, ask the user for a file path selection.
    Args: None
    """
    return filedialog.askopenfilename()

def move_file(source: str, destination: str) -> None:
    """
    Procedure moves a file from one location to another.
    Args:
        source (str): Path of the source file.
        destination (str): Path of the destination file.
    """
    try:
        # Move the file from source to destination
        shutil.move(source, destination)
        messagebox.showinfo ("Successful Movement",f"file has been relocated successfully from:\n{source}\nto:\n{destination}")
    except Exception as e:
        messagebox.showerror ("Error", f"An error occurred while moving the file: {e}")
    pass

def paths_content_list (directory_path: str) -> list[str]:
    """
    Obtains a list of paths from a given directory.
    Args:
        directory_path (str): directory to extract a list of paths.
    Returns:
        list[str]: List of paths.
    """
    # Get the absolute paths of all templates in the "Templates" directory
    return [os.path.join(directory_path, file) for file in os.listdir(directory_path)]

def get_folders_string(path: str) -> str:
    """
    Generate a string containing all the folders in the provided path, separated by a newline character.
    Args:
        path (str): Path to the directory.
    Returns:
        str: String containing all the folders in the path separated by newline character.
    """
    folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    folders_string = '\n'.join(folders)
    return folders_string

if __name__ == "__main__":
    
    "create_database () # Función validada"
    "create_template () # Función validada"

# Last code Line.