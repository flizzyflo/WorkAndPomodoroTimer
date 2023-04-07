from enum import Enum

PROGRAMM_VERSION = "1.7"
PROGRAMM_TITLE = "WorkTime Tracking"
WIDTH = 30

### Database constants
DATABASE_NAME = "/Applications/ProgrammingFiles/Python/Published/WorkTimer/src/database/work_time.db"
TABLE_NAME = "work_time_table"
EXPORT_HEADLINE = "day;month;year;hours;minutes;seconds\n"

### STYLING
FONTDICT = ('calibri', 25, 'bold')

TITLE_BACKGROUND_COLOR_FROZEN = "grey"
TITLE_BACKGROUND_COLOR_ACTIVE = "green"
TITLE_FONT_COLOR = "black"

BUTTON_STYLE = {"fg":TITLE_FONT_COLOR,
                "width" : 20,
                "activebackground" : "#eb9234" }

LABEL_STYLE_FROZEN ={"background": TITLE_BACKGROUND_COLOR_FROZEN, 
                    "foreground": TITLE_FONT_COLOR, 
                    "font": ('calibri', 30, 'bold')}

LABEL_STYLE_ACTIVE ={"background": TITLE_BACKGROUND_COLOR_ACTIVE, 
                    "foreground": TITLE_FONT_COLOR, 
                    "font": ('calibri', 30, 'bold')}

### Window Size settings
FRAMESIZE = "500x500"
MIN_SIZE= (500, 500)
MAX_SIZE= (500, 500)


class PomodoroTimes(Enum):

    """
    Pomodoro Break settings and Duration settings
    """

    LONGBREAK = 20
    SHORTBREAK = 5
    POMODOROMINUTES = 24
    POMODOROSECONDS = 60


class WorkTimeBarriers(Enum):

    """
    work time barriers
    """

    NORMAL_DAILY_WORK_TIME = 1
    MAX_DAILY_WORK_TIME = 2
