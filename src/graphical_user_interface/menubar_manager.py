import tkinter as tk
from tkinter import filedialog
from src.database.database_facade import DatabaseFacade


class MenuBarManager(tk.Menu):
    """
    Base Menuclass to handle Menu and allow the user to
    use several functionalities.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filemenu = tk.Menu(master=self)
        self.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Export file", command=lambda: self.export_database_information())
        self.filemenu.add_command(label="Settings")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=lambda: quit())
        self.db_facade: DatabaseFacade = None

    def export_database_information(self) -> None:
        self.db_facade = DatabaseFacade()
        path_to_store_file: str = filedialog.askdirectory(title="Save export to...")
        self.db_facade.export_database_entries(path_to_store_csv_file=path_to_store_file)
        self.db_facade = None

