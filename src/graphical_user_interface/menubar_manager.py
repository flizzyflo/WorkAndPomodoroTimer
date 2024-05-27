import tkinter as tk


class MenuBarManager(tk.Menu):
    """
    Base Menuclass to handle Menu and allow the user to
    use several functionalities.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filemenu = tk.Menu(master=self)
        self.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Export file")
        self.filemenu.add_command(label="Settings")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=lambda: quit())


