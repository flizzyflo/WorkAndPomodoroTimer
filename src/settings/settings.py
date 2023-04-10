from enum import Enum

# General information
PROGRAMM_VERSION: str = "1.8"
PROGRAMM_TITLE: str = "Work-time tracking"
WIDTH: int = 30


# Database constants
with open(file=r"/Applications/ProgrammingFiles/Python/Published/WorkTimer/src/database/database_filepath.txt", mode="r") as db_filepath:
    filepath = db_filepath.read()
DATABASE_NAME: str = rf"{filepath}"
TABLE_NAME: str = "work_time_table"
EXPORT_HEADLINE: str = "day;month;year;hours;minutes;seconds\n"
DATABASE_INFORMATION_FIELDS: list[str] = ["year", "month", "day", "hours", "minutes", "seconds", "description"]

# GUI-Styling
FONT_TUPLE: tuple[str, int, str] = ('calibri', 25, 'bold')

TITLE_BACKGROUND_COLOR_FROZEN: str = "grey"
TITLE_BACKGROUND_COLOR_ACTIVE: str = "green"
TITLE_FONT_COLOR: str = "black"

BUTTON_STYLE: dict[str, str | int] = {"fg": TITLE_FONT_COLOR,
                                      "width": 20,
                                      "activebackground": "#eb9234"}

LABEL_STYLE_FROZEN: dict[str, any] = {"background": TITLE_BACKGROUND_COLOR_FROZEN,
                                      "foreground": TITLE_FONT_COLOR,
                                      "font": ('calibri', 30, 'bold')}

LABEL_STYLE_ACTIVE: dict[str, any] = {"background": TITLE_BACKGROUND_COLOR_ACTIVE,
                                      "foreground": TITLE_FONT_COLOR,
                                      "font": ('calibri', 30, 'bold')}

# Window Size settings
FRAME_SIZE: str = "500x500"
MIN_SIZE: tuple[int, int] = (500, 500)
MAX_SIZE: tuple[int, int] = (500, 500)

HOUR: int = 60
MINUTE: int = 60


class PomodoroTimes(Enum):

    """
    Pomodoro Break settings and Duration settings
    """

    LONG_BREAK: int = 20
    SHORT_BREAK: int = 5
    POMODORO_MINUTES: int = 24
    POMODORO_SECONDS: int = 60


class WorkTimeBarriers(Enum):

    """
    work time barriers
    """

    NORMAL_DAILY_WORK_TIME_HOURS: int = 7
    NORMAL_DAILY_WORK_TIME_MINUTES: int = 48
    MAX_DAILY_WORK_TIME_HOURS: int = 10
    MAX_DAILY_WORK_TIME_MINUTES: int = 0
