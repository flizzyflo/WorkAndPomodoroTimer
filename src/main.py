
from src.clock.worktimeclock import WorkTimeClock


from src.menu_information_management.menuinformation import MenuInformation
from src.graphical_user_interface.graphicaluserinterface import GraphicalUserInterface


if __name__ == "__main__":

    menu_information = MenuInformation()

    clock = WorkTimeClock(initial_hours=0,
                          initial_minutes=00,
                          initial_seconds=0)

    continue_existing_worktime_data: str = "no"

    gui = GraphicalUserInterface(work_time_clock=clock)
    
    gui.mainloop()
