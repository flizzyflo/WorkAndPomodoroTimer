import getpass
import sys

from datetime import datetime

class Export:
    def create_work_time_txt(clockObject: object, filename: str = "WorkingTime"):

        if sys.platform == "win32":
            with open(rf'C:\Users\{getpass.getuser()}\Desktop\{filename}_{datetime.now().strftime(("%B"))}.txt', "a",) as file:
                file.write(f"Working Day: {datetime.now().strftime(('%d.%m.%Y'))} \tTime worked (hours: minutes: seconds): {clockObject}\n")

        else:
            pass