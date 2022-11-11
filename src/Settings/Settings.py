

PROGRAMM_VERSION = "1.7"
PROGRAMM_TITLE = "WorkTime Tracking"
WIDTH = 30

### Database constants
DATABASE_NAME = "src/WorkTimeDatabase/work_time_db.db"
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

### Window Size Settings
FRAMESIZE = "500x500"
MIN_SIZE= (500, 500)
MAX_SIZE= (500, 500)

### Pomodoro Break Settings and Duration Settings
LONGBREAK = 20
SHORTBREAK = 5
POMODOROMINUTES = 24
POMODOROSECONDS = 60

### work time barriers
NORMAL_DAILY_WORK_TIME = 8
MAX_DAILY_WORK_TIME = 10