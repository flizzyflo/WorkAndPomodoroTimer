
from pathlib import Path
from src.clock.worktimeclock import WorkTimeClock
from src.graphical_user_interface.graphicaluserinterface import GraphicalUserInterface
from src.database.database_facade import DatabaseFacade


if __name__ == "__main__":

    database_accessor = DatabaseFacade()
    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=00,
                          initial_seconds=0)

    gui = GraphicalUserInterface(work_time_clock=clock,
                                 database_facade=database_accessor)

    gui.mainloop()
