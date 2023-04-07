from random import randint
from tkinter import messagebox

class MenuInformation:

    

    def show_menubar_information() -> None:
        messagebox.showinfo("About this application...", 
                            f"""This application was programmed in Python 3.11.0 by Florian Lübke.\nThis project is explicitly seen as freeware and can be provided to anyone who is interested in it.\nEnjoy tracking your work-time!""")


    def show_version_information(current_version_number: str) -> None:
        messagebox.showinfo("Changelog & Version information", 
        f"""-Current Version: {current_version_number}: Improved class structure of timer and pomodoro class.
        \n-Version 1.6: Code Refactoring. Implemented a database to collect working time.
        \n-Version 1.5: Implemented random selection of break information shown in message window. Made application displayed always in foreground.
        \n-Version 1.4: Implementation of Pomodoro Counter as additional feature. Accessible via Settings -> Pomodoro Timer. More refactoring of code.
        \n-Version 1.3: Massive refactoring of the whole application. Made code more efficient and easier to maintain. Preliminary implementation of PomodoroClass.
        \n-Version 1.2: Added the possibility to export tracking into a .txt file which is stored at ones desktop. Accessible via 'File -> Export working time to .txt. Changed the color-style of the application. Implemented the Pomodoro-Setting Checkbox to prepare for possible Pomodoro Counter update.'
        \n-Version 1.1: Added more interaktive Buttons and a light-system with yellow and red warning lightning to indicate whether one works too long. Merged the Start and Stop Button to an interactive button.
        \n-Version 1.0: Initial creation of the whole application.""")

        
    def returnRandomBreakMessage(pomodoroObject: object):

        messages = [f"You should take a break. Your break should last {pomodoroObject.getBreakTime()} minutes. After that, you will be even more productive, I promise!",
                    f"Nothing moves us forward on our journey better than a break. Enjoy your {pomodoroObject.getBreakTime()} minutes!",
                    f"Calmness attracts life, restlessness scares it away. Be calm for at least {pomodoroObject.getBreakTime()} minutes.",
                    f"We have far too little leisure: time when nothing is going on. This is the time when the Einsteins, the creative researchers, make their discoveries. The business and the routine are uninteresting and counterproductive. Take a break for {pomodoroObject.getBreakTime()} minutes.",
                    f"What happens without rests does not last. Rest for {pomodoroObject.getBreakTime()} minutes.",
                    ]

        return messages[randint(0, len(messages) - 1)]