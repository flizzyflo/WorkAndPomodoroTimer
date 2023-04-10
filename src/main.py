import datetime
from tkinter import messagebox

from clocks.worktimeclock import WorkTimeClock
from database.databasemanager import DatabaseManager
from settings.settings import DATABASE_NAME, TABLE_NAME
from src.database.work_time_information_tuple import WorkTimeInformationTuple
from userinterface.gui import GraphicalUserInterface

if __name__ == "__main__":

    worktime_database: DatabaseManager = DatabaseManager(database_name=DATABASE_NAME,
                                                         table_name=TABLE_NAME)

    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=0,
                          initial_seconds=0)

    continue_existing_worktime_data: str = "no"

    if DatabaseManager.entry_already_exists_in(database=worktime_database):

        # grab date as db key
        current_date: str = str(datetime.date.today())
        year, month, day = current_date.split("-")

        fetched_data = worktime_database.fetch_single_entry(year_filter=year,
                                                            month_filter=month,
                                                            day_filter=day)

        # maps current values to field names
        work_time_data = WorkTimeInformationTuple(**fetched_data)

        continue_existing_worktime_data = messagebox.askquestion(title="Continue existing data",
                                                                 message=f"""Already stored data for today.
                                                \nDo you want to continue existing data?
                                                Stored data is: {int(work_time_data.hours):02.0f}:{int(work_time_data.minutes):02.0f}:{int(work_time_data.seconds):02.0f} (hh:mm:ss).
                                                \nIf 'No', it will be overriden.""")

        if continue_existing_worktime_data == "yes":

            clock.set_hours_to(hours=int(work_time_data.hours))
            clock.set_minutes_to(minutes=int(work_time_data.minutes))
            clock.set_seconds_to(seconds=int(work_time_data.seconds))

    gui = GraphicalUserInterface(work_time_clock=clock,
                                 database=worktime_database)
    
    gui.mainloop()
