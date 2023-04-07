
from src.clocks.worktimeclock import WorkTimeClock
from src.database.databasemanager import DatabaseManager
from src.settings.settings import DATABASE_NAME, TABLE_NAME
from src.userinterface.gui import GraphicalUserInterface

if __name__ == "__main__":

    database_object = DatabaseManager(database_name=DATABASE_NAME,
                                      table_name=TABLE_NAME)
    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=0,
                          initial_seconds=0)

    # pomodoro = PomodoroClock(24, 60, SHORTBREAK, LONGBREAK)

    gui = GraphicalUserInterface(clock_object=clock,
                                 database_object=database_object)
    
    gui.mainloop()