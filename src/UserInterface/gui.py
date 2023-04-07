
import datetime
import tkinter
from tkinter import Tk, BOTH, DISABLED, NORMAL, X, Button, Label, LabelFrame, messagebox, filedialog

from src.clocks.pomodoroclock import PomodoroClock
from src.clocks.worktimeclock import WorkTimeClock
from src.database.databasemanager import DatabaseManager
from src.settings.settings import PROGRAMM_TITLE, TITLE_FONT_COLOR, PROGRAMM_VERSION, FONTDICT, BUTTON_STYLE, \
    LABEL_STYLE_ACTIVE, LABEL_STYLE_FROZEN, \
    TITLE_BACKGROUND_COLOR_FROZEN, WIDTH, WorkTimeBarriers, PomodoroTimes
from src.userinterface.menuinformation import MenuInformation


class GraphicalUserInterface(Tk):

    def __init__(self,
                 clock_object: WorkTimeClock,
                 database_object: DatabaseManager,
                 pomodoroObject: PomodoroClock = None) -> None:
        
        super().__init__()
        
        self.title(PROGRAMM_TITLE)
        self.attributes("-topmost", True)

        self.database_object = database_object
        self.pomodoro_is_enabled: bool = False
        self.pomodoro_object: PomodoroClock = pomodoroObject
        self.clock_object: WorkTimeClock = clock_object
        self.current_version: str = PROGRAMM_VERSION

        self.initializeMenues()
        self.initializeWorkTimerButtons()


    def initializeMenues(self) -> None:
        """Sets up the menu bar to control the application"""

        self.menubar = tkinter.Menu(self)
        self.aboutfiles = tkinter.Menu(self.menubar)
        self.aboutfiles.add_command(label= "About", 
                                    command= lambda: MenuInformation.show_menubar_information())
        self.aboutfiles.add_command(label= "Version Information", 
                                    command= lambda: MenuInformation.show_version_information(current_version_number= self.current_version))

        self.menufiles = tkinter.Menu(self.menubar)
        self.menufiles.add_separator()
        self.menufiles.add_command(label= "Export work-time database entries", 
                                   command= lambda: self.export_data())
        
        self.menufiles.add_separator()
        self.menufiles.add_command(label= "Quit Work-Time-Tracker", 
                                   command= quit)

        # self.settingsfiles = tkinter.Menu(self.menubar)
        # self.settingsfiles.add_checkbutton(label="Pomodoro Timer", 
        #                                    state= NORMAL, 
        #                                    command= lambda: self.initializePomodoroGUI())

        self.menubar.add_cascade(label= "Database- & Program Management", 
                                 menu= self.menufiles)

        # self.menubar.add_cascade(label= "settings",
        #                          menu= self.settingsfiles)

        self.menubar.add_cascade(label= "About", 
                                 menu= self.aboutfiles)

        self.config(menu= self.menubar)

    def initializeWorkTimerButtons(self) -> None:
        """Initializes all Buttons for the work timer clock. Sets up the initial methods"""

        self.buttonFrame = LabelFrame(master= self)
        self.buttonFrame.pack(fill=BOTH, 
                              expand="yes")

        self.resultFrame = LabelFrame(master= self, 
                                      bg="grey")

        self.resultFrame.pack(fill=BOTH, 
                              expand="yes")

        self.startButton = Button(master= self.buttonFrame, 
                                  text= "Start working", 
                                  command= lambda: self.updateWorkTimeLabel(), 
                                  font= FONTDICT, 
                                  **BUTTON_STYLE, 
                                  bg= "#e87807")

        self.startButton.pack(fill= BOTH, 
                              expand= "yes")

        self.resetButton = Button(master= self.buttonFrame, 
                                  text= "Reset working time", 
                                  command= lambda: self.resetClockInterface(), 
                                  font= FONTDICT, 
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
                               text= self.clock_object, 
                               **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill= BOTH, 
                            expand= "yes")


    def export_data(self) -> None:

        """Wrapper function to call the directory selection screen and insert the path selected into the
        database object. The database object will create a csv file containing all the work data and
        store it at the path selectted."""

        filepath = filedialog.askdirectory(title="Select dir for working data export:")
        self.database_object.save_csv_file_to_path(filepath)


#################################################################
### From here on downwards are the pomodoro clock gui methods ###
#################################################################

    def initializePomodoroGUI(self) -> None:
        """Initializes the pomodoro GUI. Called via menubar"""

        if self.pomodoro_is_enabled is False:

            self.pomodoroFrame = LabelFrame(master=self,
                                            bg="grey")

            self.pomodoroFrame.pack(fill=BOTH, 
                                    expand="yes")

            self.pomodoroButton = Button(master=self.pomodoroFrame,
                                         text="Start Pomodoro",
                                         font=FONTDICT,
                                         width=10,
                                         activebackground="#eb9234",
                                         bg="#e87807",
                                         command=lambda: self.managePomodoroTimer(initial= True))
            self.pomodoroButton.pack(fill=X,
                                     expand="yes")


            self.pomodoroInformationLabel = Label(master= self.pomodoroFrame, 
                                                  text=f"Breaks: {self.pomodoro_object.getBreakCounter() }  |  Next break duration: {self.pomodoro_object.getBreakTime()} min.",
                                                  width=WIDTH,
                                                  bg=TITLE_BACKGROUND_COLOR_FROZEN,
                                                  fg=TITLE_FONT_COLOR,
                                                  font=('calibri', 15, 'bold'))
           
            self.pomodoroInformationLabel.pack(fill=X,
                                               expand="yes")
           
            self.pomodoroLabelHeader = Label(master=self.pomodoroFrame,
                                             text="Next break in: ",
                                             width=WIDTH,
                                             **LABEL_STYLE_FROZEN)
            self.pomodoroLabelHeader.pack(fill=X,
                                          expand="yes")

            self.pomodoroTimeLabel = Label(master=self.pomodoroFrame,
                                           text="25:00",
                                           width=WIDTH,
                                           **LABEL_STYLE_FROZEN)

            self.pomodoroTimeLabel.pack(fill= X, 
                                        expand="yes")

            self.startButton.config(command=lambda: self.updateBothTimers())

            self.pomodoroItems = [self.pomodoroFrame, self.pomodoroLabelHeader, self.pomodoroTimeLabel, self.pomodoroInformationLabel, self.pomodoroButton]
            self.pomodoro_is_enabled = True

        else:
            self.deactivatePomodoroGUI(minutes=PomodoroTimes.POMODOROMINUTES.value,
                                       seconds=PomodoroTimes.POMODOROSECONDS.value)


    def deactivatePomodoroGUI(self, minutes: int, seconds: int) -> None:
        """Deactivates the pomodoro GUI. Called via settings in menubar"""

        for pomodoroItem in self.pomodoroItems:
            pomodoroItem.destroy()

        self.pomodoro_object.resetClock(minutes=minutes, seconds=seconds)
        self.pomodoro_object.resetBreakCounter()

        self.pomodoro_is_enabled = False

    def countPomodoroTimer(self) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""

        self.pomodoro_object.countPomodoroTimer(seconds=60)

        if (self.pomodoro_object.getMinutes() == 0) & (self.pomodoro_object.getSeconds() == 0):
            self.stopPomodoroCounting()
    
    def updatePomodoroBackgroundColor(self, color: str) -> None:
        """Manages the background colorization of the pomodoro counter GUI."""

        self.pomodoroTimeLabel.config(text=self.pomodoro_object,
                                      bg=color)
        self.pomodoroLabelHeader.config(bg=color)
        self.pomodoroFrame.config(bg=color)
        self.pomodoroInformationLabel.config(bg=color,
                                             text=f"Breaks: {self.pomodoro_object.getBreakCounter() }  |  Next break duration: {self.pomodoro_object.getBreakTime()} min.")
            

    def stopPomodoroCounting(self):
        """Stops the count of the pomodoro counter"""
        
        self.pomodoro_object.setPomodoroActive(False)
        self.pomodoroButton.config(state=NORMAL,
                                   command=lambda: self.managePomodoroTimer(initial= True))

    def managePomodoroTimer(self, initial: bool = False) -> None:
        """Main method for updating the counting gui of the pomodoro clock. Calls several submethods."""

        if initial:
            self.pomodoroButton.config(state=DISABLED)

        self.pomodoro_object.setPomodoroActive(True)
        self.countPomodoroTimer()

        if not self.pomodoro_object.is_active():
            self.pomodoro_object.resetClock(minutes=PomodoroTimes.POMODOROMINUTES.value,
                                            seconds=PomodoroTimes.POMODOROSECONDS.value)
            self.updatePomodoroBackgroundColor(color="grey")
            self.informAboutBreak()

        else:
            self.updatePomodoroBackgroundColor(color="green")
            self.pomodoroTimeLabel.after(1000, lambda: self.managePomodoroTimer())
        
    def informAboutBreak(self):
        """Brings up a pop-up window informing a user about the necessity of a break"""

        messagebox.showwarning(title=f"Overwhelming! You are so hardworking!",
                               message=f"{MenuInformation.returnRandomBreakMessage(self.pomodoro_object)}")


##################################################################
### From here on downwards are the work time clock gui methods ###
##################################################################


    def resetClockInterface(self) -> None:
        """Stops counting of the work time counter and sets it back to its inital state."""

        self.stopCounting()
        self.clock_object.reset_clock()
        
        self.startButton.config(text="Start working", command=lambda: self.updateWorkTimeLabel())
        self.resetButton.config(state=DISABLED, bg="#FA9632")
        self.timeLabel.config(text=self.clock_object)

    def updateBackgroundColour(self) -> None:
        """Updates the background color of the work time labels depending on the working time one works"""

        if WorkTimeBarriers.MAX_DAILY_WORK_TIME.value > self.clock_object.get_hours() >= WorkTimeBarriers.NORMAL_DAILY_WORK_TIME.value:
            self.timeLabel.config(bg="yellow")
            self.timeLabelHeader.config(bg="yellow")
            self.resultFrame.config(bg="yellow")
        
        elif self.clock_object.get_hours() >= WorkTimeBarriers.MAX_DAILY_WORK_TIME.value:
            self.timeLabel.config(bg="red")
            self.timeLabelHeader.config(bg="red")
            self.resultFrame.config(bg="red")

        else:
            self.timeLabel.config(**LABEL_STYLE_ACTIVE)
            self.timeLabelHeader.config(**LABEL_STYLE_ACTIVE)
            self.resultFrame.config(bg="green")

    def updateWorkTimeLabel(self) -> None:
        """Calls several submethods. Updates the visualization of the work timer and presents 
        the actual amount of time already worked"""

        self.updateBackgroundColour()
        self.clock_object.count_time()
        self.recolorStartStopButtonText()
        self.timeLabel.config(text=self.clock_object)
        self.timeLabel.after(1000, lambda: self.updateWorkTimeLabel())


    def recolorStartStopButtonText(self) -> None:
        """Adjusts the colorization of the buttons and manages their behaviour"""

        if self.startButton.cget("text") == "Start working":
            self.startButton.config(command=lambda: self.stopCounting(), text="Take a break")
            self.resetButton.config(state=NORMAL, bg="#e87807")

        if self.startButton.cget("text") == "Continue working":
            self.startButton.config(command=lambda: self.stopCounting(), text="Take a break")


    def stopCounting(self):
        """Stops work timer from counting"""

        self.timeLabel.destroy()
        
        work_time = str(self.clock_object)
        self.timeLabel = Label(master= self.resultFrame, text= work_time, **LABEL_STYLE_FROZEN)
        self.timeLabel.pack(fill=BOTH, expand="yes")
        self.timeLabelHeader.config(bg="grey")
        self.resultFrame.config(bg="grey")

        self.database_object.maintain_database_entry(datetime.date.today(), work_time)

        if (self.pomodoro_is_enabled is True) and not self.pomodoro_object.is_active():
            self.startButton.config(command=lambda: self.updateBothTimers(), text="Continue working")

        else:
            self.startButton.config(command=lambda: self.updateWorkTimeLabel(), text="Continue working")
        self.resetButton.config(command=lambda: self.resetClockInterface())

    def updateBothTimers(self):
        """Starts both timers, pomodoro and work timer after one returns from making a break."""

        self.updateWorkTimeLabel()
        self.managePomodoroTimer(initial=True)
