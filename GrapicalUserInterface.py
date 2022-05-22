import tkinter
from tkinter import messagebox



from tkinter import *
from PomodoroClock import PomodoroClock
from Settings import *
from Clock import Clock
from MenuInformation import *
from Export import Export

class GraphicalUserInterface:

    def __init__(self, clockObject: object, pomodoroObject: object) -> None:
        self.root = Tk()
        self.root.title("WorkTime Tracking")
        self.root.geometry(frameSize)
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.iconbitmap("./clock.ico")
        self.root.attributes("-topmost", True)

        self.pomodoroActive: bool = False
        self.pomodoroObject: object = pomodoroObject
        self.clockObject: object = clockObject
        self.current_version: str = "1.5"

        self.initializeMenues()
        self.initializeWorkTimerButtons()

        self.root.mainloop()


    def initializeMenues(self) -> None:
        """Sets up the menu bar to control the application"""

        self.menubar = tkinter.Menu(self.root)
        self.aboutfiles = tkinter.Menu(self.menubar)
        self.aboutfiles.add_command(label= "About", 
                                    command= lambda: MenuInformation.show_menubar_information())
        self.aboutfiles.add_command(label= "Version Information", 
                                    command= lambda: MenuInformation.show_version_information(current_version_number= self.current_version))

        self.menufiles = tkinter.Menu(self.menubar)
        self.menufiles.add_command(label= "Export working time to .txt", 
                                   command= lambda: Export.create_work_time_txt(clockObject= self.clockObject))
        self.menufiles.add_separator()
        self.menufiles.add_command(label= "Quit Work-Time-Tracker", 
                                   command= quit)

        self.settingsfiles = tkinter.Menu(self.menubar)
        self.settingsfiles.add_checkbutton(label="Pomodoro Timer", 
                                           state= NORMAL, 
                                           command= lambda: self.initializePomodoroGUI())

        self.menubar.add_cascade(label= "File", 
                                 menu= self.menufiles)
        self.menubar.add_cascade(label= "Settings", 
                                 menu= self.settingsfiles)
        self.menubar.add_cascade(label= "About", 
                                 menu= self.aboutfiles)

        self.root.config(menu= self.menubar)


    def initializeWorkTimerButtons(self) -> None:
        """Initializes all Buttons for the work timer clock. Sets up the initial methods"""

        self.buttonFrame = LabelFrame(master= self.root)
        self.buttonFrame.pack(fill=BOTH, 
                              expand="yes")

        self.resultFrame = LabelFrame(master= self.root, 
                                      bg="grey")

        self.resultFrame.pack(fill=BOTH, 
                              expand="yes")

        self.startButton = Button(master= self.buttonFrame, 
                                  text= "Start working", 
                                  command= lambda: self.updateWorkTimeLabel(), 
                                  font= fontDict, 
                                  **BUTTON_STYLE, 
                                  bg= "#e87807")

        self.startButton.pack(fill= BOTH, 
                              expand= "yes")

        self.resetButton = Button(master= self.buttonFrame, 
                                  text= "Reset working time", 
                                  command= lambda: self.resetClockInterface(), 
                                  font= fontDict, 
                                  **BUTTON_STYLE, 
                                  bg= "#FA9632", 
                                  state= DISABLED)

        self.resetButton.pack(fill= BOTH, 
                              expand= "yes")

        self.timeLabelHeader = Label(master= self.resultFrame, 
                                     text= "Total Working Time: ", 
                                     **LABEL_STYLE_FROZEN)
        self.timeLabelHeader.pack(fill= BOTH, 
                                  expand= "yes")

        self.timeLabel = Label(master= self.resultFrame, 
                               text= "00:00:00", 
                               **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill= BOTH, 
                            expand= "yes")

### From here on downwards are the pomodoro clock gui methods

    def initializePomodoroGUI(self) -> None:
        """Initializes the pomodoro GUI. Called via menubar"""

        if self.pomodoroActive == False:

            self.pomodoroFrame = LabelFrame(master= self.root, 
                                            bg="grey")

            self.pomodoroFrame.pack(fill=BOTH, 
                                    expand="yes")

            self.pomodoroButton = Button(master= self.pomodoroFrame, 
                                         text= "Start Pomodoro", 
                                         font= fontDict, 
                                         width= 10, 
                                         activebackground = "#eb9234", 
                                         bg= "#e87807", 
                                         command= lambda: self.managePomodoroTimer(initial= True))
            self.pomodoroButton.pack(fill= X, 
                                     expand= "yes")


            self.pomodoroInformationLabel = Label(master= self.pomodoroFrame, 
                                                  text= f"Total Breaks: {self.pomodoroObject.getBreakCounter() }  |  Next break duration: {self.pomodoroObject.getBreakTime()} min.", 
                                                  width= width, 
                                                  bg= TITLE_BACKGROUND_COLOR_FROZEN, 
                                                  fg= TITLE_FONT_COLOR, 
                                                  font= ('calibri', 15, 'bold'))
           
            self.pomodoroInformationLabel.pack(fill= X, 
                                               expand= "yes")
           
            self.pomodoroLabelHeader = Label(master= self.pomodoroFrame, 
                                             text= "Next break in: ", 
                                             width= width, 
                                             **LABEL_STYLE_FROZEN)
            self.pomodoroLabelHeader.pack(fill= X, 
                                          expand= "yes")

            self.pomodoroTimeLabel = Label(master= self.pomodoroFrame, 
                                           text= "25:00", 
                                           width= width, 
                                           **LABEL_STYLE_FROZEN)

            self.pomodoroTimeLabel.pack(fill= X, 
                                        expand= "yes")

            self.startButton.config(command= lambda: self.updateBothTimer())

            self.pomodoroItems = [self.pomodoroFrame, self.pomodoroLabelHeader, self.pomodoroTimeLabel, self.pomodoroInformationLabel, self.pomodoroButton]
            self.pomodoroActive = True

        else:
            self.deactivatePomodoroGUI(minutes= POMODOROMINUTES, seconds= POMODOROSECONDS)


    def deactivatePomodoroGUI(self, minutes: int, seconds: int) -> None:
        """Deactivates the pomodoro GUI. Called via settings in menubar"""

        for pomodoroItem in self.pomodoroItems:
            pomodoroItem.destroy()

        self.pomodoroObject.resetClock(minutes= minutes, seconds= seconds)
        self.pomodoroObject.resetBreakCounter()

        self.pomodoroActive = False


    def countPomodoroTimer(self) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""

        self.pomodoroObject.countPomodoroTimer(seconds= 60)

        if (self.pomodoroObject.getMinutes() == 0) & (self.pomodoroObject.getSeconds() == 0):
            self.stopPomodoroCounting()
    

    def updatePomodoroBackgroundColor(self, color: str) -> None:
        """Manages the background colorization of the pomodoro counter GUI."""

        self.pomodoroTimeLabel.config(text= self.pomodoroObject,  
                                      bg= color)
        self.pomodoroLabelHeader.config(bg= color)
        self.pomodoroFrame.config(bg= color)
        self.pomodoroInformationLabel.config(bg= color, 
                                             text= f"Breaks: {self.pomodoroObject.getBreakCounter() }  |  Next break duration: {self.pomodoroObject.getBreakTime()} min.")
            

    def stopPomodoroCounting(self):
        """Stops the count of the pomodoro counter"""
        
        self.pomodoroObject.setPomodoroActive(False)
        self.pomodoroButton.config(state= NORMAL, command= lambda: self.managePomodoroTimer(initial= True))


    def managePomodoroTimer(self, initial: bool = False) -> None:
        """Main method for updating the counting gui of the pomodoro clock. Calls several submethods."""

        if initial:
            self.pomodoroButton.config(state= DISABLED)

        self.pomodoroObject.setPomodoroActive(True)
        self.countPomodoroTimer()

        if self.pomodoroObject.getPomodoroActive() == False:
            self.pomodoroObject.resetClock(minutes= POMODOROMINUTES, seconds= POMODOROSECONDS)
            self.updatePomodoroBackgroundColor(color= "grey")
            self.informAboutBreak()

        else:
            self.updatePomodoroBackgroundColor(color= "green")
            self.pomodoroTimeLabel.after(1000, lambda: self.managePomodoroTimer())
        

    def informAboutBreak(self):
        """Brings up a pop up window informing a user about the necessity of a break"""

        messagebox.showwarning(title= f"Overwhelming! You are so hardworking!", 
                               message= f"{returnRandomBreakMessage(self.pomodoroObject)}")

##################################################################
### From here on downwards are the work time clock gui methods ###
##################################################################

    def resetClockInterface(self) -> None:
        """Stops counting of the work time counter and sets it back to its inital state."""

        self.stopCounting()
        self.clockObject.resetClock()
        
        self.startButton.config(text="Start working", command=lambda: self.updateWorkTimeLabel())
        self.resetButton.config(state=DISABLED, bg="#FA9632")
        self.timeLabel.config(text= self.clockObject)


    def updateBackgroundColour(self) -> None:
        """Updates the background color of the work time labels depending on the working time one works"""

        if 10 > self.clockObject.getHours() >= 8:
            self.timeLabel.config(bg="yellow")
            self.timeLabelHeader.config(bg= "yellow")
            self.resultFrame.config(bg= "yellow")
        
        elif self.clockObject.getHours() >= 10:
            self.timeLabel.config(bg="red")
            self.timeLabelHeader.config(bg= "red")
            self.resultFrame.config(bg= "red")

        else:
            self.timeLabel.config(**LABEL_STYLE_ACTIVE)
            self.timeLabelHeader.config(**LABEL_STYLE_ACTIVE)
            self.resultFrame.config(bg = "green")


    def updateWorkTimeLabel(self) -> None:
        """Calls several submethods. Updates the visualization of the work timer and presents 
        the actual amount of time already worked"""

        self.updateBackgroundColour()
        self.clockObject.countWorkTime()
        self.adaptStartStopButtonText()
        self.timeLabel.config(text= self.clockObject)
        self.timeLabel.after(1000, lambda: self.updateWorkTimeLabel())


    def adaptStartStopButtonText(self) -> None:
        """Adjusts the colorization of the buttons and manages their behaviour"""

        if self.startButton.cget("text") == "Start working":
            self.startButton.config(command=lambda: self.stopCounting(), text="Take a break")
            self.resetButton.config(state=NORMAL, bg="#e87807")

        if self.startButton.cget("text") == "Continue working":
            self.startButton.config(command=lambda: self.stopCounting(), text="Take a break")


    def stopCounting(self):
        """Stops work timer from counting"""

        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        
        self.timeLabel = Label(master= self.resultFrame, text= self.clockObject, **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill=BOTH, expand="yes")
        self.timeLabelHeader.config(bg="grey")
        self.resultFrame.config(bg="grey")

        if (self.pomodoroActive == True) and (self.pomodoroObject.getPomodoroActive() == False):
            self.startButton.config(command=lambda: self.updateBothTimer(), text="Continue working")

        else:
            self.startButton.config(command=lambda: self.updateWorkTimeLabel(), text="Continue working")
        self.resetButton.config(command=lambda: self.resetClockInterface())


    def updateBothTimer(self):
        """Starts both timers, pomodoro and work timer after one returns from amking a break."""

        self.updateWorkTimeLabel()
        self.managePomodoroTimer(initial= True)


def main() -> None:
    cl = Clock()
    pm = PomodoroClock()
    gui = GraphicalUserInterface(cl, pm)

main()