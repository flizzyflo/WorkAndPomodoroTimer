import tkinter

from tkinter import *
from PomodoroClock import PomodoroClock
from Settings import *
from Clock import Clock
from MenuInformation import *
from Export import Export

class GraphicalUserInterface:


    def __init__(self, clockObject: object, pomodoroObject: object):
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
        self.current_version = "1.3"

        self.initializeMenues()
        self.initializeButtons()

        self.root.mainloop()


    def initializeButtons(self):
        self.buttonFrame = LabelFrame(master= self.root)
        self.buttonFrame.pack(fill=BOTH, expand="yes")

        self.resultFrame = LabelFrame(master= self.root, bg="grey")
        self.resultFrame.pack(fill=BOTH, expand="yes")

        self.startButton = Button(master= self.buttonFrame, text="Start counting working time", command=lambda: self.updateWorkTimeLabel(), font= fontDict, **BUTTON_STYLE, bg= "#e87807")
        self.startButton.pack(fill=BOTH, expand="yes")

        self.stopButton = Button(master= self.buttonFrame, text="Reset working time", command=lambda: self.resetClockInterface(), font= fontDict, **BUTTON_STYLE, bg="#FA9632", state=DISABLED)
        self.stopButton.pack(fill=BOTH, expand="yes")

        self.timeLabelHeader = Label(master= self.resultFrame, text="Total Working Time: ", **LABEL_STYLE_FROZEN)
        self.timeLabelHeader.pack(fill=BOTH, expand="yes")

        self.timeLabel = Label(master=self.resultFrame, text="00:00:00", **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill=BOTH, expand="yes")


    def initializeMenues(self):
        
        self.menubar = tkinter.Menu(self.root)
        self.aboutfiles = tkinter.Menu(self.menubar)
        self.aboutfiles.add_command(label="About", command=lambda: MenuInformation.show_menubar_information())
        self.aboutfiles.add_command(label="Version Information", command=lambda: MenuInformation.show_version_information(self.current_version))

        self.menufiles = tkinter.Menu(self.menubar)
        self.menufiles.add_command(label="Export working time to .txt", command= lambda: Export.create_work_time_txt(self.clockObject))
        self.menufiles.add_separator()
        self.menufiles.add_command(label="Quit Work-Time-Tracker", command=quit)

        self.settingsfiles = tkinter.Menu(self.menubar)
        self.settingsfiles.add_checkbutton(label="Pomodoro Timer", state= NORMAL, command= lambda: self.initializePomodoro())

        self.menubar.add_cascade(label="File", menu=self.menufiles)
        self.menubar.add_cascade(label="Settings", menu=self.settingsfiles)
        self.menubar.add_cascade(label="About", menu=self.aboutfiles)

        self.root.config(menu= self.menubar)


    def initializePomodoro(self):

        if self.pomodoroActive == False:

            self.pomodoroFrame = LabelFrame(master= self.root, bg="grey")
            self.pomodoroFrame.pack(fill=BOTH, expand="yes")

            self.pomodoroLabelHeader = Label(master= self.pomodoroFrame, text="Next break in: ", width=width, **LABEL_STYLE_FROZEN)
            self.pomodoroLabelHeader.pack(fill=X, expand="yes")

            self.pomodoroLabel = Label(master= self.pomodoroFrame, text="00:00", width=width, **LABEL_STYLE_FROZEN)
            self.pomodoroLabel.pack(fill=X, expand="yes")

            self.pomodoroLabel = Label(master= self.pomodoroFrame, text=f"Current short breaks: {self.pomodoroObject.getBreakCounter() }  |  Current Break Duration: {self.pomodoroObject.getBreakTime()} min", width=width, bg= TITLE_BACKGROUND_COLOR_FROZEN, 
                    fg= TITLE_FONT_COLOR, 
                    font= ('calibri', 15, 'bold'))
            self.pomodoroLabel.pack(fill=X, expand="yes")
            
            self.pomodoroButton = Button(master= self.pomodoroFrame, text= "Start Pomodoro Timer", font= fontDict, width= 10, activebackground = "#eb9234", bg= "#e87807")
            self.pomodoroButton.pack(fill=X, expand="yes")

            self.pomodoroItems = [self.pomodoroFrame, self.pomodoroLabelHeader, self.pomodoroLabel, self.pomodoroButton]
            self.pomodoroActive = True

        else:
            self.deactivatePomodoro()


    def deactivatePomodoro(self):

        for pomodoroItem in self.pomodoroItems:
            pomodoroItem.destroy()

        self.pomodoroActive = False


    def resetClockInterface(self):
        
        self.stopCounting()
        self.clockObject.resetClock()

        self.startButton.config(text="Start counting working time", command=lambda: self.updateWorkTimeLabel())
        self.stopButton.config(state=DISABLED, bg="#FA9632")
        self.timeLabel.config(text=self.clockObject)


    def updateBackgroundColour(self):
        self.timeLabel.config(**LABEL_STYLE_ACTIVE)
        self.timeLabelHeader.config(**LABEL_STYLE_ACTIVE)
        self.resultFrame.config(bg = "green")


    def checkTimePomodoro(self) -> None:
        pass


    def checkTimeWorkTimer(self, clockObject: object):

        if clockObject.getSeconds() == 60:
            clockObject.increaseMinutes()
            clockObject.setSeconds()

        else:
            clockObject.increaseSeconds()

        if clockObject.getMinutes() == 60:
            clockObject.increaseHours()
            clockObject.setMinutes()


    def updateWorkTimeLabel(self) -> None:

        self.updateBackgroundColour()
        self.checkTimeWorkTimer(clockObject= self.clockObject)
        self.checkStartButtonText()
        self.timeLabel.config(text= self.clockObject)
        self.timeLabel.after(1000, lambda: self.updateWorkTimeLabel())


    def checkStartButtonText(self) -> None:

        if self.startButton.cget("text") == "Start counting working time":
            self.startButton.config(command=lambda: self.stopCounting(), text="Stop counting working time")
            self.stopButton.config(state=NORMAL, bg="#e87807")

        if self.startButton.cget("text") == "Restart counting working time":
            self.startButton.config(command=lambda: self.stopCounting(), text="Stop counting working time")


    def stopCounting(self) -> None:

        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        self.timeLabel.destroy()
        

        self.timeLabel = Label(master= self.resultFrame, text= self.clockObject, **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill=BOTH, expand="yes")
        self.startButton.config(command=lambda: self.updateWorkTimeLabel(), text="Restart counting working time")
        self.timeLabelHeader.config(bg="grey")
        self.resultFrame.config(bg="grey")


def main():
    cl = Clock()
    pm = PomodoroClock()
    gui = GraphicalUserInterface(cl, pm)

main()