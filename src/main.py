
from src.clock.worktimeclock import WorkTimeClock
from src.database.database_connector import DatabaseConnector
from src.graphical_user_interface.graphicaluserinterface import GraphicalUserInterface


if __name__ == "__main__":

    #database_connector = DatabaseConnector.get_database_connection(database_path="to_be_passed_in")
    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=00,
                          initial_seconds=0)


    gui = GraphicalUserInterface(work_time_clock=clock)
    
    gui.mainloop()
