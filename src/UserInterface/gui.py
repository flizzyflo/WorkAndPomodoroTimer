
import datetime
import tkinter
from tkinter import Tk, BOTH, DISABLED, NORMAL, X, Button, Label, LabelFrame, messagebox, filedialog

from src.clocks.pomodoroclock import PomodoroClock
from src.clocks.worktimeclock import WorkTimeClock
from src.database.databasemanager import DatabaseManager
from src.settings.settings import PROGRAMM_TITLE, TITLE_FONT_COLOR, PROGRAMM_VERSION, FONT_TUPLE, BUTTON_STYLE, \
    LABEL_STYLE_ACTIVE, LABEL_STYLE_FROZEN, \
    TITLE_BACKGROUND_COLOR_FROZEN, WIDTH, WorkTimeBarriers, PomodoroTimes
from src.userinterface.menuinformation import MenuInformation


class GraphicalUserInterface(Tk):

    def __init__(self,
                 work_time_clock: WorkTimeClock,
                 database: DatabaseManager,
                 pomodoro_object: PomodoroClock = None) -> None:
        
        super().__init__()
        
        self.title(PROGRAMM_TITLE)
        self.attributes("-topmost", True)

        self.database = database
        self.work_time_clock: WorkTimeClock = work_time_clock
        self.pomodoro_is_enabled: bool = False
        self.pomodoro_object: PomodoroClock = pomodoro_object
        self.current_program_version: str = PROGRAMM_VERSION
        self.menubar: tkinter.Menu = None
        self.about_menu: tkinter.Menu = None
        self.database_menu: tkinter.Menu = None

        self.pomodoro_frame = tkinter.LabelFrame = None
        self.pomodoro_button = tkinter.Button = None
        self.pomodoro_information_label: tkinter.Label = None
        self.pomodoro_label_header: tkinter.Label = None
        self.pomodoro_time_label: tkinter.Label = None
        self.pomodoro_items: list[tkinter.Label | tkinter.Button] = None

        self.button_frame: tkinter.LabelFrame = None
        self.work_time_frame: tkinter.LabelFrame = None
        self.start_button: tkinter.Button = None
        self.reset_button: tkinter.Button = None

        self.work_time_headline_label: tkinter.Label = None
        self.worked_time_label: tkinter.Label = None

        self.initialize_menues()
        self.initialize_buttons()

    def initialize_menues(self) -> None:
        """Sets up the menu bar to control the application"""

        self.menubar = tkinter.Menu(master=self)
        self.about_menu = tkinter.Menu(master=self.menubar)

        self.about_menu.add_command(label="About",
                                    command=lambda: MenuInformation.show_menubar_information())
        self.about_menu.add_command(label="Version Information",
                                    command=lambda: MenuInformation.show_version_information(current_version_number=self.current_program_version))

        self.database_menu = tkinter.Menu(self.menubar)
        self.database_menu.add_separator()
        self.database_menu.add_command(label="Export work-time database entries",
                                       command=lambda: self.export_data())

        self.database_menu.add_separator()
        self.database_menu.add_command(label="Quit Work-Time-Tracker",
                                       command=lambda: quit())

        self.menubar.add_cascade(label="Database- & Program Management",
                                 menu=self.database_menu)

        self.menubar.add_cascade(label="About",
                                 menu=self.about_menu)

        self.config(menu=self.menubar)

    def initialize_buttons(self) -> None:
        """Initializes all Buttons for the work timer clock. Sets up the initial methods"""

        self.button_frame = LabelFrame(master=self)
        self.button_frame.pack(fill=BOTH,
                               expand=1)

        self.work_time_frame = LabelFrame(master=self,
                                          bg="grey")

        self.work_time_frame.pack(fill=BOTH,
                                  expand=1)

        self.start_button = Button(master=self.button_frame,
                                   text="Start working",
                                   command=lambda: self.update_worked_time_label(),
                                   font=FONT_TUPLE,
                                   **BUTTON_STYLE,
                                   bg="#e87807")

        self.start_button.pack(fill=BOTH,
                               expand=1)

        self.reset_button = Button(master=self.button_frame,
                                   text="Reset working time",
                                   command=lambda: self.reset_work_timer(),
                                   font=FONT_TUPLE,
                                   **BUTTON_STYLE,
                                   bg="#FA9632",
                                   state=DISABLED)

        self.reset_button.pack(fill=BOTH,
                               expand=1)

        self.work_time_headline_label = Label(master=self.work_time_frame,
                                              text="Total Working Time: ",
                                              **LABEL_STYLE_FROZEN)
        self.work_time_headline_label.pack(fill=BOTH,
                                           expand=1)

        self.worked_time_label = Label(master=self.work_time_frame,
                                       text=self.work_time_clock.__repr__(),
                                       **LABEL_STYLE_FROZEN)
        self.worked_time_label.pack(fill=BOTH,
                                    expand=1)

    def export_data(self) -> None:

        """
        Wrapper function to call the directory selection screen and insert the path selected into the
        database object. The database object will create a csv file containing all the work data and
        store it at the path selected.
        """

        filepath = filedialog.askdirectory(title="Select directory to store working data export at:")
        self.database.save_csv_file_to_path(path=filepath)

    def initialize_pomodoro(self) -> None:

        """Initializes the pomodoro GUI. Called via menubar"""

        if self.pomodoro_is_enabled is False:

            self.pomodoro_frame = LabelFrame(master=self,
                                             bg="grey")

            self.pomodoro_frame.pack(fill=BOTH,
                                     expand=1)

            self.pomodoro_button = Button(master=self.pomodoro_frame,
                                          text="Start Pomodoro",
                                          font=FONT_TUPLE,
                                          width=10,
                                          activebackground="#eb9234",
                                          bg="#e87807",
                                          command=lambda: self.update_pomodoro_timer(initial=True))
            self.pomodoro_button.pack(fill=X,
                                      expand=1)

            self.pomodoro_information_label = Label(master=self.pomodoro_frame,
                                                    text=f"""Breaks: {self.pomodoro_object.get_break_counter() }  
                                                  |  Next break duration: {self.pomodoro_object.get_break_time_short()}
                                                   min.""",
                                                    width=WIDTH,
                                                    bg=TITLE_BACKGROUND_COLOR_FROZEN,
                                                    fg=TITLE_FONT_COLOR,
                                                    font=('calibri', 15, 'bold'))
           
            self.pomodoro_information_label.pack(fill=X,
                                                 expand=1)
           
            self.pomodoro_label_header = Label(master=self.pomodoro_frame,
                                               text="Next break in: ",
                                               width=WIDTH,
                                               **LABEL_STYLE_FROZEN)
            self.pomodoro_label_header.pack(fill=X,
                                            expand=1)

            self.pomodoro_time_label = Label(master=self.pomodoro_frame,
                                             text="25:00",
                                             width=WIDTH,
                                             **LABEL_STYLE_FROZEN)

            self.pomodoro_time_label.pack(fill=X,
                                          expand=1)

            self.start_button.config(command=lambda: self.update_timers())

            self.pomodoro_items = [self.pomodoro_frame, self.pomodoro_label_header, self.pomodoro_time_label, self.pomodoro_information_label, self.pomodoro_button]
            self.pomodoro_is_enabled = True

        else:
            self.deactivate_pomodoro(minutes=PomodoroTimes.POMODORO_MINUTES.value,
                                     seconds=PomodoroTimes.POMODORO_SECONDS.value)

    def deactivate_pomodoro(self, minutes: int, seconds: int) -> None:
        """Deactivates the pomodoro GUI. Called via settings in menubar"""

        for pomodoroItem in self.pomodoro_items:
            pomodoroItem.destroy()

        self.pomodoro_object.reset_clock()
        self.pomodoro_object.reset_break_counter()

        self.pomodoro_is_enabled = False

    def count_pomodoro(self) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""

        self.pomodoro_object.count_pomodoro_timer(seconds=60)

        if (self.pomodoro_object.get_minutes() == 0) & (self.pomodoro_object.get_seconds() == 0):
            self.stop_pomodoro_counting()
    
    def update_pomodoro_background(self, color: str) -> None:
        """Manages the background colorization of the pomodoro counter GUI."""

        self.pomodoro_time_label.config(text=self.pomodoro_object.__repr__(),
                                        bg=color)
        self.pomodoro_label_header.config(bg=color)
        self.pomodoro_frame.config(bg=color)
        self.pomodoro_information_label.config(bg=color,
                                               text=f"""Breaks: {self.pomodoro_object.get_break_counter() }  
                                             |  Next break duration: {self.pomodoro_object.get_break_time_short()} 
                                             min.""")
            
    def stop_pomodoro_counting(self):
        """Stops the count of the pomodoro counter"""
        
        self.pomodoro_object.set_pomodoro_active_to(active=False)
        self.pomodoro_button.config(state=NORMAL,
                                    command=lambda: self.update_pomodoro_timer(initial=True))

    def update_pomodoro_timer(self, initial: bool = False) -> None:
        """Main method for updating the counting gui of the pomodoro clock. Calls several sub-methods."""

        if initial:
            self.pomodoro_button.config(state=DISABLED)

        self.pomodoro_object.set_pomodoro_active_to(active=True)
        self.count_pomodoro()

        if not self.pomodoro_object.pomodoro_is_active():
            self.pomodoro_object.reset_clock()
            self.update_pomodoro_background(color="grey")
            self.show_break()

        else:
            self.update_pomodoro_background(color="green")
            self.pomodoro_time_label.after(1000, lambda: self.update_pomodoro_timer())
        
    def show_break(self):
        """Brings up a pop-up window informing a user about the necessity of a break"""

        messagebox.showwarning(title=f"Overwhelming! You are so hardworking!",
                               message=f"{MenuInformation.returnRandomBreakMessage(self.pomodoro_object)}")

    def reset_work_timer(self) -> None:
        """Stops counting of the work time counter and sets it back to its inital state."""

        self.stop_counting_work_time()
        self.work_time_clock.reset_clock()
        
        self.start_button.config(text="Start working",
                                 command=lambda: self.update_worked_time_label())
        self.reset_button.config(state=DISABLED,
                                 bg="#FA9632")
        self.worked_time_label.config(text=self.work_time_clock.__repr__())

    def is_doing_overtime(self) -> bool:
        reached_overtime_minutes: bool = self.work_time_clock.get_minutes() >= WorkTimeBarriers.NORMAL_DAILY_WORK_TIME_MINUTES.value
        reached_overtime_hours: bool = self.work_time_clock.get_hours() >= WorkTimeBarriers.NORMAL_DAILY_WORK_TIME_HOURS.value
        if reached_overtime_hours and reached_overtime_minutes:
            return True

        else:
            return False

    def reached_worktime_maximum(self) -> bool:
        reached_maximum_worktime_minutes: bool = self.work_time_clock.get_minutes() >= WorkTimeBarriers.MAX_DAILY_WORK_TIME_MINUTES.value
        reached_maximum_worktime_hours: bool = self.work_time_clock.get_hours() >= WorkTimeBarriers.MAX_DAILY_WORK_TIME_HOURS.value

        if reached_maximum_worktime_hours and reached_maximum_worktime_minutes:
            return True

        else:
            return False

    def update_worktimer_background(self) -> None:
        """Updates the background color of the work time labels depending on the working time one works"""

        if self.is_doing_overtime() and not self.reached_worktime_maximum():
            self.worked_time_label.config(bg="yellow")
            self.work_time_headline_label.config(bg="yellow")
            self.work_time_frame.config(bg="yellow")
        
        elif self.reached_worktime_maximum():
            self.worked_time_label.config(bg="red")
            self.work_time_headline_label.config(bg="red")
            self.work_time_frame.config(bg="red")

        else:
            self.worked_time_label.config(**LABEL_STYLE_ACTIVE)
            self.work_time_headline_label.config(**LABEL_STYLE_ACTIVE)
            self.work_time_frame.config(bg="green")

    def update_worked_time_label(self) -> None:
        """Calls several submethods. Updates the visualization of the work timer and presents 
        the actual amount of time already worked"""

        self.update_worktimer_background()
        self.work_time_clock.count_time()
        self.recolor_start_button()
        self.worked_time_label.config(text=self.work_time_clock.__repr__())
        self.worked_time_label.after(1000, lambda: self.update_worked_time_label())

    def recolor_start_button(self) -> None:
        """Adjusts the colorization of the buttons and manages their behaviour"""

        if self.start_button.cget("text") == "Start working":
            self.start_button.config(command=lambda: self.stop_counting_work_time(),
                                     text="Take a break")
            self.reset_button.config(state=NORMAL,
                                     bg="#e87807")

        if self.start_button.cget("text") == "Continue working":
            self.start_button.config(command=lambda: self.stop_counting_work_time(),
                                     text="Take a break")

    def stop_counting_work_time(self):
        """Stops work timer from counting"""

        self.worked_time_label.destroy()
        
        work_time = str(self.work_time_clock)
        self.worked_time_label = Label(master=self.work_time_frame,
                                       text=work_time, **LABEL_STYLE_FROZEN)
        self.worked_time_label.pack(fill=BOTH,
                                    expand=1)
        self.work_time_headline_label.config(bg="grey")
        self.work_time_frame.config(bg="grey")

        self.database.maintain_database_entry(datetime.date.today(), work_time)

        if (self.pomodoro_is_enabled is True) and not self.pomodoro_object.pomodoro_is_active():
            self.start_button.config(command=lambda: self.update_timers(),
                                     text="Continue working")

        else:
            self.start_button.config(command=lambda: self.update_worked_time_label(),
                                     text="Continue working")
        self.reset_button.config(command=lambda: self.reset_work_timer())

    def update_timers(self):
        """Starts both timers, pomodoro and work timer after one returns from making a break."""

        self.update_worked_time_label()
        self.update_pomodoro_timer(initial=True)
