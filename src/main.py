import datetime
from tkinter import messagebox

from clocks.worktimeclock import WorkTimeClock
from database.databasemanager import DatabaseManager
from settings.settings import DATABASE_NAME, TABLE_NAME
from userinterface.gui import GraphicalUserInterface

if __name__ == "__main__":

    worktime_database: DatabaseManager = DatabaseManager(database_name=DATABASE_NAME,
                                                         table_name=TABLE_NAME)

    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=0,
                          initial_seconds=0)

    continue_existing_worktime_data: str = "no"

    if DatabaseManager.entry_already_exist(database_object=worktime_database):

        # grab date as db key
        current_date: str = str(datetime.date.today())
        year, month, day = current_date.split("-")

        fetched_data = worktime_database.fetch_single_entry(year_filter=year,
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

            clock.set_hours_to(hours=int(stored_hours))
            clock.set_minutes_to(minutes=int(stored_minutes))
            clock.set_seconds_to(seconds=int(stored_seconds))

    gui = GraphicalUserInterface(work_time_clock=clock,
                                 database=worktime_database)
    
    gui.mainloop()
