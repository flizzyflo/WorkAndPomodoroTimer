import tkinter as tk
from tkinter import filedialog
from src.database.database_facade import DatabaseFacade
from src.graphical_user_interface.settingsmenu import SettingsMenu
from src.menu_information_management.menuinformation import MenuInformation
from src.settings.settings import PROGRAM_VERSION


class MenuBarManager(tk.Menu):
    """
    Base Menuclass to handle Menu and allow the user to
    use several functionalities.
    """

    db_facade: DatabaseFacade

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filemenu = tk.Menu(master=self)
        self.add_cascade(label="File",
                         menu=self.filemenu)
        self.filemenu.add_command(label="Export work time",
                                  command=lambda: self.export_database_information())
        self.filemenu.add_command(label="Settings",
                                  command=lambda: SettingsMenu())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",
                                  command=lambda: quit())
        self.information_menu = tk.Menu(master=self)
        self.add_cascade(label="Information", menu=self.information_menu)
        self.information_menu.add_command(label="Application information",
                                          command=lambda: MenuInformation.show_menubar_information())
        self.information_menu.add_command(label="Version information",
                                          command=lambda: MenuInformation.show_version_information(PROGRAM_VERSION))
        self.db_facade = None

    def export_database_information(self) -> None:
        self.db_facade = DatabaseFacade()
        path_to_store_file: str = filedialog.askdirectory(title="Select destination path")
        self.db_facade.export_database_entries(path_to_store_csv_file=path_to_store_file)
        self.db_facade = None

