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
        self.current_version: str = "1.3"

        self.initializeMenues()
        self.initializeButtons()

        self.root.mainloop()


    def initializeButtons(self) -> None:
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


    def initializeMenues(self) -> None:
        
        self.menubar = tkinter.Menu(self.root)
        self.aboutfiles = tkinter.Menu(self.menubar)
        self.aboutfiles.add_command(label="About", command=lambda: MenuInformation.show_menubar_information())
        self.aboutfiles.add_command(label="Version Information", command=lambda: MenuInformation.show_version_information(current_version_number= self.current_version))

        self.menufiles = tkinter.Menu(self.menubar)
        self.menufiles.add_command(label="Export working time to .txt", command= lambda: Export.create_work_time_txt(clockObject= self.clockObject))
        self.menufiles.add_separator()
        self.menufiles.add_command(label="Quit Work-Time-Tracker", command=quit)

        self.settingsfiles = tkinter.Menu(self.menubar)
        self.settingsfiles.add_checkbutton(label="Pomodoro Timer", state= NORMAL, command= lambda: self.initializePomodoro())

        self.menubar.add_cascade(label="File", menu=self.menufiles)
        self.menubar.add_cascade(label="Settings", menu=self.settingsfiles)
        self.menubar.add_cascade(label="About", menu=self.aboutfiles)

        self.root.config(menu= self.menubar)


    def initializePomodoro(self) -> None:

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
            
            self.pomodoroButton = Button(master= self.pomodoroFrame, text= "Start Pomodoro", font= fontDict, width= 10, activebackground = "#eb9234", bg= "#e87807", command= lambda: self.updatePomodoroTimeLabel(clockObject= self.pomodoroObject, timeLabel= self.pomodoroTimeLabel, informationLabel = self.pomodoroInformationLabel, timeLabelHeader= self.pomodoroLabelHeader, resultFrame= self.pomodoroFrame, pomodoroButton= self.pomodoroButton))
            self.pomodoroButton.pack(fill=X, expand="yes")

            self.pomodoroItems = [self.pomodoroFrame, self.pomodoroLabelHeader, self.pomodoroTimeLabel, self.pomodoroInformationLabel, self.pomodoroButton]
            self.pomodoroActive = True

        else:
            self.deactivatePomodoro()


    def deactivatePomodoro(self) -> None:

        for pomodoroItem in self.pomodoroItems:
            pomodoroItem.destroy()

        self.pomodoroActive = False


    def resetClockInterface(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        
        timeLabel = self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        clockObject.resetClock()
        
        self.startButton.config(text="Start working", command=lambda: self.updateWorkTimeLabel(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame))
        self.resetButton.config(state=DISABLED, bg="#FA9632")
        timeLabel.config(text= clockObject)


    def updateBackgroundColour(self, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:
        timeLabel.config(**LABEL_STYLE_ACTIVE)
        timeLabelHeader.config(**LABEL_STYLE_ACTIVE)
        resultFrame.config(bg = "green")


    def checkTimePomodoro(self) -> None:
        pass


    def checkTimeWorkTimer(self, clockObject: object) -> None:

        if clockObject.getSeconds() == 60:
            clockObject.increaseMinutes()
            clockObject.setSeconds()

        else:
            clockObject.increaseSeconds()

        if clockObject.getMinutes() == 60:
            clockObject.increaseHours()
            clockObject.setMinutes()


    def updatePomodoroTimeLabel(self, clockObject: object, timeLabel: object, informationLabel: object, timeLabelHeader: object, resultFrame: object, pomodoroButton: object) -> None:
        
        if (clockObject.getMinutes() == 0) & (clockObject.getSeconds() == 0):
            clockObject.setSeconds()
            clockObject.setMinutes()
            clockObject.increaseBreakCounter()
        
        elif clockObject.getSeconds() == 0:
            clockObject.decreaseMinutes()
            clockObject.setSeconds()
        
        else:
            clockObject.decreaseSeconds()
        

        timeLabel.config(text= clockObject, bg="green")
        timeLabelHeader.config(bg="green")
        resultFrame.config(bg="green")
        informationLabel.config(bg="green", text= f"Breaks: {self.pomodoroObject.getBreakCounter() }  |  Recommended break duration: {self.pomodoroObject.getBreakTime()} min")
        pomodoroButton.config(state= DISABLED, bg="#FA9632")
        
        timeLabel.after(1000, lambda: self.updatePomodoroTimeLabel(clockObject= clockObject, timeLabel= timeLabel, informationLabel= informationLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame, pomodoroButton= pomodoroButton))
        

    def updateWorkTimeLabel(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:

        self.updateBackgroundColour(timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        self.checkTimeWorkTimer(clockObject= clockObject)
        self.checkStartButtonText(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame)
        timeLabel.config(text= clockObject)
        timeLabel.after(1000, lambda: self.updateWorkTimeLabel(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame))


    def checkStartButtonText(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> None:

        if self.startButton.cget("text") == "Start working":
            self.startButton.config(command=lambda: self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame), text="Stop counting")
            self.resetButton.config(state=NORMAL, bg="#e87807")

        if self.startButton.cget("text") == "Restart counting":
            self.startButton.config(command=lambda: self.stopCounting(clockObject= clockObject, timeLabel= timeLabel, timeLabelHeader= timeLabelHeader, resultFrame= resultFrame), text="Stop counting")


    def stopCounting(self, clockObject: object, timeLabel: object, timeLabelHeader: object, resultFrame: object) -> object:

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