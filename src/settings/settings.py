from enum import Enum

PROGRAMM_VERSION: str = "1.7"
PROGRAMM_TITLE: str = "WorkTime Tracking"
WIDTH: int = 30

### Database constants
DATABASE_NAME: str = "/Applications/ProgrammingFiles/Python/Published/WorkTimer/src/database/work_time.db"
TABLE_NAME: str = "work_time_table"
EXPORT_HEADLINE: str = "day;month;year;hours;minutes;seconds\n"

### STYLING
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

### Window Size settings
FRAMESIZE: str = "500x500"
MIN_SIZE: tuple[int, int] = (500, 500)
MAX_SIZE: tuple[int, int] = (500, 500)

HOUR: int = 60
MINUTE: int = 60


class PomodoroTimes(Enum):

    """
    Pomodoro Break settings and Duration settings
    """

    LONGBREAK: int = 20
    SHORTBREAK: int = 5
    POMODOROMINUTES: int = 24
    POMODOROSECONDS: int = 60


class WorkTimeBarriers(Enum):

    """
    work time barriers
    """

    NORMAL_DAILY_WORK_TIME_HOURS: int = 7
    NORMAL_DAILY_WORK_TIME_MINUTES: int = 48
    MAX_DAILY_WORK_TIME_HOURS: int = 10
    MAX_DAILY_WORK_TIME_MINUTES: int = 0
