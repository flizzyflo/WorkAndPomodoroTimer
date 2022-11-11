
from Clocks.Clock import Clock
from UserInterface.GrapicalUserInterface import GraphicalUserInterface
from WorkTimeDatabase.DatabaseManager import DatabaseManager
from Clocks.PomodoroClock import PomodoroClock
from Settings.Settings import LONGBREAK, SHORTBREAK, DATABASE_NAME, TABLE_NAME

if __name__ == "__main__":

    database_object = DatabaseManager(database_name= DATABASE_NAME, table_name= TABLE_NAME)
    clock = Clock()
    # pomodoro = PomodoroClock(24, 60, SHORTBREAK, LONGBREAK)
    gui = GraphicalUserInterface(clock_object=clock, database_object= database_object)
    
    gui.mainloop()