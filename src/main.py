
from src.clock.worktimeclock import WorkTimeClock
from src.graphical_user_interface.graphicaluserinterface import GraphicalUserInterface
from src.database.database_facade import DatabaseFacade


if __name__ == "__main__":

    database_accessor = DatabaseFacade(database_path=r"/Applications/ProgrammingFiles/Python/Published/WorkTimer/src/database/test2.db")
    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=00,
                          initial_seconds=0)

    gui = GraphicalUserInterface(work_time_clock=clock,
                                 database_facade=database_accessor)
    
    gui.mainloop()
