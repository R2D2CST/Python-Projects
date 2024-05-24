# We import native python libraries.
import sys, os
import tkinter as tk
from tkinter import filedialog, messagebox
""" Native Library Comments: 
sys, os: libraries used to manage the operative system.
tkinter (tk): main library to handle widgets and guided user interface for the application.
"""

# I import my own developed functions and procedures.
from lib import lib
from lib import statistics
""" My Own Library Comments:
lib is the folder where I store the module lib: where I am storing functionalities not related
with the execution of this guided user interface.
"""

class main_window (tk.Tk):
    """
    Window class where the template generator will interact with the user in order to render
    the template documents.
    """

    def __init__(self) -> None:
        """
        Method to initiate the main window class object, we use a object programming oriented
        method in order to use functions or procedures top or button in the code with no problem
        in order to create widgets or destroy them as we interact with the application. 
        Args: None
        """
        # We inherit all the supper class attributes and methods from Tk.
        super().__init__()
        
        # I build my class attributes form this point.
        self.script_directory:str = self.program_path ()
        self.projects_paths = lib.join_paths (self.script_directory, "Projects")
        lib.verify_path (self.projects_paths)
        
        self.temp_string_var = ""

        # I define the attributes my application window will have.
        self.title ("template-automate version (2.0.0)")
        self.geometry ("400x600")
        self.minsize (400, 400)
        self.icon_path = lib.join_paths (self.script_directory, "gui/Gondor.ico")
        self.iconbitmap (self.icon_path)

        # I define the menu bar that will create and delete widgets in our workspace frame.
        self.menu_bar = tk.Menu (self)
        self.load_menubar ()
        self.config (menu= self.menu_bar)

        # I create the work space where all the widgets will be placed.
        self.work_space = tk.Frame (self)
        self.work_space.pack ()

        # I start the main loop where the application will be self build.
        self.mainloop ()
        pass
    
    # From here I will define the dynamic methods and functions, in order to have a cleaner code. 
    def load_menubar (self)->None:
        """
        This procedure will be used to build the menu bar in our main application and manage what
        widgets we desire to see at the time.
        """
        # I build the About or Help Menu.
        about_menu = tk.Menu (self.menu_bar, tearoff= 0)
        self.menu_bar.add_cascade (label= "Help", menu= about_menu)
        about_menu.add_command (label= "About Application", command= lambda: print ("About Application"))
        about_menu.add_command (label= "User Manual", command= lambda: print ("Open Instructions"))

        # I build the Example creator for Templates or Data Bases.
        create_templates_menu = tk.Menu (self.menu_bar, tearoff= 0)
        self.menu_bar.add_cascade (label= "Create Example Templates", menu= create_templates_menu)
        create_templates_menu.add_command (label= "Create Data Base", command= lib.create_database)
        create_templates_menu.add_command (label= "Create Template", command= lib.create_template)
        
        # I build the Render Projects Section (for creating, editing or rendering a project).
        render_project_menu = tk.Menu (self.menu_bar, tearoff= 0)
        self.menu_bar.add_cascade (label= "Render Projects", menu= render_project_menu)
        render_project_menu.add_command (label= "Create Render Project", command= self.load_create_project)
        render_project_menu.add_command (label= "Edit Render Project", command= self.load_edit_project)
        render_project_menu.add_command (label= "Render a Project", command= self.load_render_project)
        pass

    def delete_workspace (self)->None:
        """
        This procedure will delete all the widgets with in the work space.
        """
        [self.work_space.winfo_children()[frame].destroy() for frame in range(len(self.work_space.winfo_children()))]
        pass

    def check_projects_stored (self)->None:
        """
        Procedure executes a function that builds a string list for each project in the application program,
        and latter shows them in the label templates_in_project.
        """
        global templates_in_project
        projects_list = lib.get_folders_string (path= self.projects_paths)
        templates_in_project.config (text= projects_list)
        pass

    def create_project_button_action (self)->None:
        """
        The purpose of this method is to define the procedure that will take action when pushing
        the create project button.
        """
        global project_name_entry
        # We create the project architecture path.
        project_name = project_name_entry.get ()
        lib.create_project_architecture (self.projects_paths, project_name)
        self.check_projects_stored ()
        pass

    def append_template_into_project (self)->None:
        """
        Procedure moves a selected template given by the user and moves it into the templates folder
        in the Project folder path in the application.
        """
        global project_name_entry

        # I build the path for the given project.
        project_name = project_name_entry.get ()
        if project_name == "":
            messagebox.showerror ("Error", "No project has been typed.")
            return
        project_path =lib.join_paths (self.projects_paths, project_name)
        templates_path =lib.join_paths (project_path, "Templates")
        # I ask the user to select the document to upload.
        origin_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
        if origin_path == "":
            messagebox.showerror ("Error", "Canceled operation.")
            return
        lib.move_file (source= origin_path, destination= templates_path)
        pass

    def append_database_into_project (self)->None:
        """
        Procedure moves a selected database given by the user and moves it into the database folder
        in the Project folder path in the application.
        """
        global project_name_entry

        # I build the path for the given project.
        project_name = project_name_entry.get ()
        if project_name == "":
            messagebox.showerror ("Error", "No project has been typed.")
            return
        project_path =lib.join_paths (self.projects_paths, project_name)
        templates_path =lib.join_paths (project_path, "Data Base")
        # I ask the user to select the document to upload.
        origin_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if origin_path == "":
            messagebox.showerror ("Error", "Canceled operation.")
            return
        lib.move_file (source= origin_path, destination= templates_path)
        pass

    def load_create_project (self)->None:
        """
        This procedure will create and load all the widgets for creating a project into the application,
        and elements to interact for the user on a project.
        """
        global project_name_entry
        global templates_in_project

        # First I ensure the workspace is free to add up the following widgets.
        self.delete_workspace ()
        # I build the workspace where all this widgets will be placed.
        frame = tk.Frame (master= self.work_space)
        # I create the widgets to place later on the workspace frame.
        step1_label = tk.Label (master= frame, text= "Step 1: Create a Project Path.")
        project_name_label = tk.Label (master= frame, text= "Project Name:")
        project_name_entry = tk.Entry (master= frame)
        create_project_button = tk.Button (
            master= frame,
            text= "Create Project",
            command= self.create_project_button_action
        )
        
        step2_label = tk.Label (
            master=frame,
            text= "Step 2: Add Template(s) into the Project Path.\n(Please Note Templates Will Be Added To Named Project Above)"
        )
        templates_added_label = tk.Label (master= frame, text= f"Projects in Application:")
        templates_in_project = tk.Label (master= frame, text= "")
        self.check_projects_stored ()
        add_template_button = tk.Button (
            master= frame,
            text= f"Add Template to Project:",
            command= self.append_template_into_project
        )

        step3_label = tk.Label (
            master=frame,
            text= "Step 3: Add a database into the Project Path.\n(Please Note the Database Will Be Added To Named Project Above)"
        )
        add_database_button = tk.Button (
            master= frame,
            text= f"Add Data Base to Project:",
            command= self.append_database_into_project
        )

        # I load the widgets into the workspace frame.
        frame.pack ()
        step1_label.grid (column= 0, row= 0, pady= 5, padx= 5, columnspan=2, rowspan= 1)
        project_name_label.grid (column= 0, row= 1, pady= 5, padx= 5, columnspan=1, rowspan= 1)
        project_name_entry.grid (column= 1, row= 1, pady= 5, padx= 5, columnspan=1, rowspan= 1)
        create_project_button.grid (column= 0, row= 2, pady= 5, padx= 5, columnspan=2, rowspan= 1)

        step2_label.grid (column= 0, row= 3, pady= 5, padx= 5, columnspan=2, rowspan= 1)
        templates_added_label.grid (column= 0, row= 4, pady= 5, padx= 5, columnspan=1, rowspan= 1)
        templates_in_project.grid (column= 1, row= 4, pady= 5, padx= 5, columnspan=1, rowspan= 1)
        add_template_button.grid (column= 0, row= 5, pady= 5, padx= 5, columnspan=2, rowspan= 1)

        step3_label.grid (column= 0, row= 6, pady= 5, padx= 5, columnspan=2, rowspan= 1)
        add_database_button.grid (column= 0, row= 8, pady= 5, padx= 5, columnspan=2, rowspan= 1)
        
        pass

    def load_edit_project (self):
        """
        This procedure will create and load all the widgets for editing a project into the application,
        and elements to interact for the user on a project.
        """
        # First I ensure the workspace is free to add up the following widgets.
        self.delete_workspace ()
        # I build the workspace where all this widgets will be placed.
        frame = tk.Frame (master= self.work_space)
        # I load the widgets into the workspace frame.
        frame.pack ()
        pass

    def load_render_project (self):
        """
        This procedure will create and load all the widgets for rendering a project into the application,
        and elements to interact for the user on a project.
        """
        # First I ensure the workspace is free to add up the following widgets.
        self.delete_workspace ()
        # I build the workspace where all this widgets will be placed.
        frame = tk.Frame (master= self.work_space)
        # I load the widgets into the workspace frame.
        frame.pack ()
        pass

    # Form here onward I will define the static methods in order to have a clean code.
    @staticmethod
    def program_path ()->str:
        """
        This function gets the path where the program is executing, this path will be an absolute
        path to the file in order to get files and saving elements. 
        """
        # We get the absolute path where the program will be executed.
        if getattr(sys, 'frozen', False):
            # If the program has been packed for distribution follows this path.
            script_directory = os.path.dirname(sys.executable)
        else:
            # If program is been executed as a python file.
            script_directory = os.path.dirname(os.path.abspath(__file__))
        return script_directory

    pass

if __name__ == "__main__":
    # Ejecutamos la ventana de nuestra aplicación
    main_window ()

# Last code Line.