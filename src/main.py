import datetime
from tkinter import messagebox

from src.clocks.worktimeclock import WorkTimeClock
from src.database.databasemanager import DatabaseManager
from src.settings.settings import DATABASE_NAME, TABLE_NAME
from src.userinterface.gui import GraphicalUserInterface

if __name__ == "__main__":

    database_object: DatabaseManager = DatabaseManager(database_name=DATABASE_NAME,
                                                       table_name=TABLE_NAME)

    continue_existing_worktime_data: str = "no"

    if DatabaseManager.data_already_exist(database_object=database_object):
        current_date: str = str(datetime.date.today())
        year, month, day = current_date.split("-")
        fetched_data = database_object.fetch_single_entry(year_filter=year,
                                                          month_filter=month,
                                                          day_filter=day)[0]

        # grab hours, minutes and seconds from data tuple
        stored_hours, stored_minutes, stored_seconds = fetched_data[3:]

        continue_existing_worktime_data = messagebox.askquestion(title="Continue existing data",
                                                                 message=f"""Already stored data for today.
                                                \nDo you want to continue existing data?
                                                Stored data is: {int(stored_hours):02.0f} : {int(stored_minutes):02.0f}
                                                : {int(stored_seconds):02.0f} (hh:mm:ss).
                                                \nIf 'No', it will be overriden.""")

        if continue_existing_worktime_data == "yes":

            clock = WorkTimeClock(initial_hours=int(stored_hours),
                                  initial_minutes=int(stored_minutes),
                                  initial_seconds=int(stored_seconds))

    # no information stored according current date or no desire to continue existing information
    if not DatabaseManager.data_already_exist(database_object=database_object) or continue_existing_worktime_data == "no":
        clock = WorkTimeClock(initial_hours=0,
                              initial_minutes=59,
                              initial_seconds=57)

    # pomodoro = PomodoroClock(24, 60, SHORTBREAK, LONGBREAK)

    gui = GraphicalUserInterface(clock_object=clock,
                                 database_object=database_object)
    
    gui.mainloop()
