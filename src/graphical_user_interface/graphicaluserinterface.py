
import tkinter
from tkinter import Tk, BOTH, DISABLED, NORMAL, Button, Label, LabelFrame
from typing import Literal

from src.clock.worktimeclock import WorkTimeClock
from src.database.database_facade import DatabaseFacade
from src.settings.settings import PROGRAMM_TITLE, PROGRAMM_VERSION, FONT_TUPLE, BUTTON_STYLE, \
    LABEL_STYLE_FROZEN, WorkTimeBarriers


class GraphicalUserInterface(Tk):

    def __init__(self,
                 work_time_clock: WorkTimeClock,
                 database_facade: DatabaseFacade = None) -> None:
        
        super().__init__()
        
        self.title(PROGRAMM_TITLE)
        self.attributes("-topmost", True)

        self.database_facade: DatabaseFacade = database_facade
        self.work_time_clock: WorkTimeClock = work_time_clock
        self.current_program_version: str = PROGRAMM_VERSION
        self.stopped = False

        self.button_frame: tkinter.LabelFrame = None
        self.work_time_frame: tkinter.LabelFrame = None
        self.start_button: tkinter.Button = None
        self.reset_button: tkinter.Button = None
        self.work_time_headline_label: tkinter.Label = None
        self.worked_time_label: tkinter.Label = None

        self.initialize_buttons()

    def initialize_buttons(self) -> None:

        """
        Initializes all Buttons for the work timer clock. Sets up the initial methods
        """

        self.button_frame = LabelFrame(master=self)
        self.button_frame.pack(fill=BOTH,
                               expand=1)

        self.work_time_frame = LabelFrame(master=self,
                                          bg="grey")

        self.work_time_frame.pack(fill=BOTH,
                                  expand=1)

        self.start_button = Button(master=self.button_frame,
                                   text="Start working",
                                   command=lambda: self.start_working(),
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

    def destroy(self) -> None:

        """
        Closes the application when 'x' button is clicked. Stores the current last time into the database, even
        when time was not stopped.
        :return: None
        """

        # TODO Add question for entering description into database and add to database methods as well

        work_time = str(self.work_time_clock)

        self.database_facade.insert_data_into_database(worktime=work_time)
        self.database_facade.tt()
        super().destroy()

    def reset_work_timer(self) -> None:

        """
        Stops counting of the work time counter and sets it back to its inital state.
        """

        self.stop_working()
        self.work_time_clock.reset_clock()
        
        self.start_button.config(text="Start working",
                                 command=lambda: self.start_working())
        self.reset_button.config(state=DISABLED,
                                 bg="#FA9632")
        self.worked_time_label.config(text=self.work_time_clock.__repr__())
        self.stopped = False

    def __is_doing_overtime(self) -> bool:

        """Checks whether one is already doing overtime or not and returns either true or false"""

        current_minutes_worked: int = int(self.work_time_clock.get_current_time())
        current_overtime_barrier: int = int(f"""{WorkTimeBarriers.NORMAL_DAILY_WORK_TIME_HOURS.value:02.0f}{WorkTimeBarriers.NORMAL_DAILY_WORK_TIME_MINUTES.value:02.0f}{WorkTimeBarriers.NORMAL_DAILY_WORK_TIME_SECONDS.value:02.0f}""")

        return current_minutes_worked >= current_overtime_barrier

    def __is_above_maximum_worktime(self) -> bool:

        """
        Checks whether one is already working than max allowed worktime is and returns either true or false
        """

        current_minutes_worked: int = int(self.work_time_clock.get_current_time())
        current_maximum_worktime_barrier: int = int(f"""{WorkTimeBarriers.MAX_DAILY_WORK_TIME_HOURS.value:02.0f}{WorkTimeBarriers.MAX_DAILY_WORK_TIME_MINUTES.value:02.0f}{WorkTimeBarriers.MAX_DAILY_WORK_TIME_SECONDS.value:02.0f}""")

        return current_minutes_worked >= current_maximum_worktime_barrier

    def __change_worktimer_background_color(self, new_color: Literal['green', 'yellow', 'red', 'grey']):

        """
        Changes the backgroundcolor of the whole work time clock to the desired color passed in as parameter
        """

        self.worked_time_label.config(bg=new_color)
        self.work_time_headline_label.config(bg=new_color)
        self.work_time_frame.config(bg=new_color)

    def change_worktimer_background_color(self) -> None:

        """
        Updates the background color of the work time labels depending on the current working time
        Overtime is yellow, above maximum allowed time is red, everything else is green
        """

        if self.__is_above_maximum_worktime():
            self.__change_worktimer_background_color(new_color="red")
        
        elif self.__is_doing_overtime() and not self.__is_above_maximum_worktime():
            self.__change_worktimer_background_color(new_color="yellow")

        else: # normal case, no overtime or max time
            self.__change_worktimer_background_color(new_color="green")

    def start_working(self) -> None:

        """
        Wrapper-method to call several sub-methods. Updates the visualization of the work timer and presents
        the actual amount of time already worked
        """

        self.change_worktimer_background_color()  # manage the gui colorization depending on the current worktime and the overtime settings
        self.work_time_clock.count_time()  # clock method to count the time

        self.__manage_start_button()  # manages the start button text and colorization
        self.worked_time_label.config(text=self.work_time_clock.__repr__())  # inserts the current work time into the label
        self.worked_time_label.after(1000, lambda: self.start_working())  # update loop for the text label

    def __manage_start_button(self) -> None:

        """
        Method to manage the text and methods of the buttons and the state of whether the
        counting was stopped or not
        :return: Nothing
        """

        if self.stopped:  # already started counting is stopped
            self.start_button.config(command=lambda: self.start_working(),
                                     text="Continue working")
            self.stopped = False

        else:  # Counting is initially started
            self.start_button.config(command=lambda: self.stop_working(),
                                     text="Take a break")

        self.reset_button.config(state=NORMAL,
                                 bg="#e87807",
                                 command=lambda: self.reset_work_timer())

    def stop_working(self):

        """
        Wrapper method which stops work timer from counting
        """
        self.stopped = True
        self.__recolor_stopped_gui()

        # TODO insert new database writer class methods.
        # self.database_writer.maintain_database_entry(date=datetime.date.today(), work_time_duration=work_time)

        self.__manage_start_button()

    def __recolor_stopped_gui(self):

        """
        Changes the gui colors when work time counting is stopped
        """

        self.worked_time_label.destroy()

        work_time = str(self.work_time_clock)

        self.worked_time_label = Label(master=self.work_time_frame,
                                       text=work_time,
                                       **LABEL_STYLE_FROZEN)
        self.worked_time_label.pack(fill=BOTH,
                                    expand=1)
        self.__change_worktimer_background_color(new_color="grey")

