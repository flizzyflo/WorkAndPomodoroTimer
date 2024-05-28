
from src.clock.worktimeclock import WorkTimeClock
from src.graphical_user_interface.graphicaluserinterface import GraphicalUserInterface
from src.database.database_facade import DatabaseFacade
from src.graphical_user_interface.menubar_manager import MenuBarManager

if __name__ == "__main__":

    database_accessor = DatabaseFacade()
    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=0,
                          initial_seconds=0)

    gui = GraphicalUserInterface(work_time_clock=clock,
                                 database_facade=database_accessor)

    mb = MenuBarManager(gui)
    gui.config(menu=mb)
    gui.mainloop()
