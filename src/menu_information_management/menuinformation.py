from tkinter import messagebox


class MenuInformation:

    @staticmethod
    def show_menubar_information() -> None:
        messagebox.showinfo("About this application...", 
                            f"""This application was programmed in Python 3.11.4 by Florian Lübke.
                            \nThis project is explicitly seen as freeware and can be provided to anyone who is 
                            interested in it.\nEnjoy tracking your work-time!""")

    @staticmethod
    def show_version_information(current_version_number: str) -> None:
        messagebox.showinfo("Changelog & Version information", 
        f"""-Current Version: {current_version_number}: Finalized settings menu, implemented settings menu.
        \n-Version 1.9: Extracted work-time-settings to JSON File. Allows management by user easily
        Implemented settings Menu for persistent setting management
        \n-Version 1.8: Massive code refactoring, implemented hour-/minute 
        boundaries, improved counting logic, added possibility to continue existing worktime data.
        \n-Version 1.7: Improved class structure of timer and pomodoro class.
        \n-Version 1.6: Code Refactoring. Implemented a database to collect working time.
        \n-Version 1.5: Implemented random selection of break information shown in message window. 
        Made application displayed always in foreground.
        \n-Version 1.4: Implementation of Pomodoro Counter as additional feature. 
        Accessible via Settings -> Pomodoro Timer. More refactoring of code.
        \n-Version 1.3: Massive refactoring of the whole application. 
        Made code more efficient and easier to maintain. Preliminary implementation of PomodoroClass.
        \n-Version 1.2: Added the possibility to export tracking into a .txt file which is stored at ones desktop. 
        Accessible via 'File -> Export working time to .txt. Changed the color-style of the application. 
        Implemented the Pomodoro-Setting Checkbox to prepare for possible Pomodoro Counter update. 
        - CURRENTLY NOT ACTIVE'
        \n-Version 1.1: Added more interactive Buttons and a light-system with yellow and red warning lightning 
        to indicate whether one works too long. Merged the Start and Stop Button to an interactive button.
        \n-Version 1.0: Initial creation of the whole application.""")
