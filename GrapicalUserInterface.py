import tkinter

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
        self.root.attributes("-topmost", False)

        self.pomodoroActive: bool = False
        self.pomodoroObject: object = pomodoroObject
        self.clockObject: object = clockObject
        self.current_version: str = "1.4"

        self.initializeMenues()
        self.initializeWorkTimerButtons()

        self.root.mainloop()


    def initializeMenues(self) -> None:
        """Sets up the menu bar to control the application"""

        self.menubar = tkinter.Menu(self.root)
        self.aboutfiles = tkinter.Menu(self.menubar)
        self.aboutfiles.add_command(label="About", command=lambda: MenuInformation.show_menubar_information())
        self.aboutfiles.add_command(label="Version Information", command=lambda: MenuInformation.show_version_information(current_version_number= self.current_version))

        self.menufiles = tkinter.Menu(self.menubar)
        self.menufiles.add_command(label="Export working time to .txt", command= lambda: Export.create_work_time_txt(clockObject= self.clockObject))
        self.menufiles.add_separator()
        self.menufiles.add_command(label="Quit Work-Time-Tracker", command=quit)

        self.settingsfiles = tkinter.Menu(self.menubar)
        self.settingsfiles.add_checkbutton(label="Pomodoro Timer", state= NORMAL, command= lambda: self.initializePomodoroGui())

        self.menubar.add_cascade(label="File", menu=self.menufiles)
        self.menubar.add_cascade(label="Settings", menu=self.settingsfiles)
        self.menubar.add_cascade(label="About", menu=self.aboutfiles)

        self.root.config(menu= self.menubar)


    def initializeWorkTimerButtons(self) -> None:
        """Initializes all Buttons for the work timer clock. Sets up the initial methods"""

        self.buttonFrame = LabelFrame(master= self.root)
        self.buttonFrame.pack(fill=BOTH, expand="yes")

        self.resultFrame = LabelFrame(master= self.root, bg="grey")
        self.resultFrame.pack(fill=BOTH, expand="yes")

        self.startButton = Button(master= self.buttonFrame, text="Start working", command=lambda: self.updateWorkTimeLabel(clockObject= self.clockObject, timeLabel= self.timeLabel, timeLabelHeader= self.timeLabelHeader, resultFrame= self.resultFrame), font= fontDict, **BUTTON_STYLE, bg= "#e87807")
        self.startButton.pack(fill=BOTH, expand="yes")

        self.resetButton = Button(master= self.buttonFrame, text="Reset working time", command=lambda: self.resetClockInterface(clockObject= self.clockObject, timeLabel= self.timeLabel, timeLabelHeader= self.timeLabelHeader, resultFrame= self.resultFrame), font= fontDict, **BUTTON_STYLE, bg="#FA9632", state=DISABLED)
        self.resetButton.pack(fill=BOTH, expand="yes")

        self.timeLabelHeader = Label(master= self.resultFrame, text="Total Working Time: ", **LABEL_STYLE_FROZEN)
        self.timeLabelHeader.pack(fill=BOTH, expand="yes")

        self.timeLabel = Label(master=self.resultFrame, text="00:00:00", **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill=BOTH, expand="yes")


    def initializePomodoroGui(self) -> None:
        """Initializes the pomodoro GUI. Called via menubar"""

        if self.pomodoroActive == False:

            self.pomodoroFrame = LabelFrame(master= self.root, bg="grey")
            self.pomodoroFrame.pack(fill=BOTH, expand="yes")

            self.pomodoroLabelHeader = Label(master= self.pomodoroFrame, text="Next break in: ", width=width, **LABEL_STYLE_FROZEN)
            self.pomodoroLabelHeader.pack(fill=X, expand="yes")

            self.pomodoroTimeLabel = Label(master= self.pomodoroFrame, text="00:00", width=width, **LABEL_STYLE_FROZEN)
            self.pomodoroTimeLabel.pack(fill=X, expand="yes")

            self.pomodoroInformationLabel = Label(master= self.pomodoroFrame, text=f"Breaks: {self.pomodoroObject.getBreakCounter() }  |  Recommended break duration: {self.pomodoroObject.getBreakTime()} min", width=width, bg= TITLE_BACKGROUND_COLOR_FROZEN, 
                    fg= TITLE_FONT_COLOR, 
                    font= ('calibri', 15, 'bold'))
            self.pomodoroInformationLabel.pack(fill=X, expand="yes")
            
            self.pomodoroButton = Button(master= self.pomodoroFrame, text= "Start Pomodoro", font= fontDict, width= 10, activebackground = "#eb9234", bg= "#e87807", command= lambda: self.updatePomodoroTimeLabel(pomodoroClockObject= self.pomodoroObject, pomodoroTimeLabel= self.pomodoroTimeLabel, pomodoroIinformationLabel = self.pomodoroInformationLabel, pomodoroTimeLabelHeader= self.pomodoroLabelHeader, pomodoroResultFrame= self.pomodoroFrame, pomodoroButton= self.pomodoroButton))
            self.pomodoroButton.pack(fill=X, expand="yes")

            self.pomodoroItems = [self.pomodoroFrame, self.pomodoroLabelHeader, self.pomodoroTimeLabel, self.pomodoroInformationLabel, self.pomodoroButton]
            self.pomodoroActive = True

        else:
            self.deactivatePomodoro(pomodoroObject= self.pomodoroObject)


    def deactivatePomodoro(self, pomodoroObject: object) -> None:
        """Deactivates the pomodoro GUI. Called via settings in menubar"""

        for pomodoroItem in self.pomodoroItems:
            pomodoroItem.destroy()

        pomodoroObject.resetClock()
        pomodoroObject.resetBreakCounter()

        self.pomodoroActive = False


    def stopPomodoroCount(self, pomodoroObject: object, pomodoroButton: object) -> None:
        """Stops the pomodoro count. Resets the values and the button to start next
        pomodoro cycle"""

        pomodoroObject.setSeconds()
        pomodoroObject.setMinutes()
        pomodoroObject.increaseBreakCounter()
        pomodoroObject.resetClock()
       

    def updatePomodoroTimerClock(self, pomodoroObject: object, pomodoroButton: object) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""

        if (pomodoroObject.getMinutes() == 0) & (pomodoroObject.getSeconds() == 0):
            self.stopPomodoroCount(pomodoroObject= pomodoroObject, pomodoroButton= pomodoroButton)
        
        elif pomodoroObject.getSeconds() == 0:
            pomodoroObject.decreaseMinutes()
            pomodoroObject.setSeconds()
        
        else:
            pomodoroObject.decreaseSeconds()


    def updatePomodorBackgroundColor(self, pomodoroObject: object, pomodoroTimeLabel: object, pomodoroTimeLabelHeader: object, pomodoroResultFrame: object, pomodoroInformationLabel: object, pomodoroButton: object) -> None:
        """Manages the background colorization of the pomodoro counter GUI."""

        if pomodoroObject.getPomodoroActive():
            pomodoroTimeLabel.config(text= pomodoroObject, bg="green")
            pomodoroTimeLabelHeader.config(bg="green")
            pomodoroResultFrame.config(bg="green")
            pomodoroInformationLabel.config(bg="green", text= f"Breaks: {self.pomodoroObject.getBreakCounter() }  |  Recommended break duration: {self.pomodoroObject.getBreakTime()} min")
            pomodoroButton.config(state= DISABLED, bg="#FA9632")


    def updatePomodoroTimeLabel(self, pomodoroClockObject: object, pomodoroTimeLabel: object, pomodoroIinformationLabel: object, pomodoroTimeLabelHeader: object, pomodoroResultFrame: object, pomodoroButton: object) -> None:
        """Main method for counting the clock. Calls several submethods."""

        pomodoroClockObject.setPomodoroActive(True)
        self.updatePomodoroTimerClock(pomodoroObject= pomodoroClockObject, pomodoroButton= pomodoroButton)
        self.updatePomodorBackgroundColor(pomodoroObject= pomodoroClockObject, pomodoroTimeLabel= pomodoroTimeLabel, pomodoroInformationLabel= pomodoroIinformationLabel, pomodoroTimeLabelHeader= pomodoroTimeLabelHeader, pomodoroResultFrame= pomodoroResultFrame, pomodoroButton= pomodoroButton)        
        pomodoroTimeLabel.after(1000, lambda: self.updatePomodoroTimeLabel(pomodoroClockObject= pomodoroClockObject, pomodoroTimeLabel= pomodoroTimeLabel, pomodoroIinformationLabel= pomodoroIinformationLabel, pomodoroTimeLabelHeader= pomodoroTimeLabelHeader, pomodoroResultFrame= pomodoroResultFrame, pomodoroButton= pomodoroButton))


    def resetClockInterface(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        """Stops counting of the work time counter and sets it back to its inital state."""

        timeLabel = self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        clockObject.resetClock()
        
        self.startButton.config(text="Start working", command=lambda: self.updateWorkTimeLabel(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame))
        self.resetButton.config(state=DISABLED, bg="#FA9632")
        timeLabel.config(text= clockObject)


    def updateBackgroundColour(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        """Updates the background color of the work time labels depending on the working time one works"""

        if 10 > clockObject.getHours() >= 8:
            timeLabel.config(bg="yellow")
            timeLabelHeader.config(bg= "yellow")
            resultFrame.config(bg= "yellow")
        
        elif clockObject.getHours() >= 10:
            timeLabel.config(bg="red")
            timeLabelHeader.config(bg= "red")
            resultFrame.config(bg= "red")

        else:
            timeLabel.config(**LABEL_STYLE_ACTIVE)
            timeLabelHeader.config(**LABEL_STYLE_ACTIVE)
            resultFrame.config(bg = "green")


    def updateWorkTimerClock(self, clockObject: object) -> None:
        """Main method to count and get information of the work time clock object
        about the work time itself."""

        if clockObject.getSeconds() == 60:
            clockObject.increaseMinutes()
            clockObject.setSeconds()

        else:
            clockObject.increaseSeconds()

        if clockObject.getMinutes() == 60:
            clockObject.increaseHours()
            clockObject.setMinutes()


    def updateWorkTimeLabel(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        """Calls several submethods. Updates the visualization of the work timer and presents 
        the actual amount of time already worked"""

        self.updateBackgroundColour(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        self.updateWorkTimerClock(clockObject= clockObject)
        self.adaptStartStopButtonText(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        timeLabel.config(text= clockObject)
        timeLabel.after(1000, lambda: self.updateWorkTimeLabel(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame))


    def adaptStartStopButtonText(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        """Adjusts the colorization of the buttons and manages their behaviour"""

        if self.startButton.cget("text") == "Start working":
            self.startButton.config(command=lambda: self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame), text="Stop counting")
            self.resetButton.config(state=NORMAL, bg="#e87807")

        if self.startButton.cget("text") == "Restart counting":
            self.startButton.config(command=lambda: self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame), text="Stop counting")


    def stopCounting(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> object:
        """Stops work timer from counting"""

        timeLabel.destroy()
        timeLabel.destroy()
        timeLabel.destroy()
        timeLabel.destroy()
        timeLabel.destroy()
        
        timeLabel = Label(master= resultFrame, text= clockObject, **LABEL_STYLE_FROZEN)
        timeLabel.pack(fill=BOTH, expand="yes")
        timeLabelHeader.config(bg="grey")
        resultFrame.config(bg="grey")

        self.startButton.config(command=lambda: self.updateWorkTimeLabel(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame), text="Restart counting")
        self.resetButton.config(command=lambda: self.resetClockInterface(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame))

        return timeLabel


def main() -> None:
    cl = Clock()
    pm = PomodoroClock()
    gui = GraphicalUserInterface(cl, pm)

main()