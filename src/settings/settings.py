from typing import List, Tuple, Dict

# General information
PROGRAM_VERSION: str = "2.0"
PROGRAM_TITLE: str = "Work-time tracking"
WIDTH: int = 30

# GUI-Styling
FONT_TUPLE: Tuple[str, int, str] = ('arial', 35, 'bold')

TITLE_BACKGROUND_COLOR_FROZEN: str = "grey"
TITLE_BACKGROUND_COLOR_ACTIVE: str = "green"
TITLE_FONT_COLOR: str = "black"

BUTTON_STYLE: Dict[str, str | int] = {"fg": TITLE_FONT_COLOR,
                                      "width": 20,
                                      "activebackground": "#eb9234"}

LABEL_STYLE_FROZEN: Dict[str, any] = {"background": TITLE_BACKGROUND_COLOR_FROZEN,
                                      "foreground": TITLE_FONT_COLOR,
                                      "font": ('calibri', 30, 'bold')}

LABEL_STYLE_ACTIVE: Dict[str, any] = {"background": TITLE_BACKGROUND_COLOR_ACTIVE,
                                      "foreground": TITLE_FONT_COLOR,
                                      "font": ('calibri', 30, 'bold')}
LABEL_WIDTH: int = 15
ENTRY_WIDTH: int = 5
PADY: int = 10
PADX: int = 10
SETTING_TIME_LABEL_NAMES: List[str] = ["Usual daily hours: ",
                                       "Usual daily minutes: ",
                                       "Max daily hours: ",
                                       "Max daily minutes: "]
# Window Size settings
FRAME_SIZE: str = "500x500"
MIN_SIZE: Tuple[int, int] = (500, 500)
MAX_SIZE: Tuple[int, int] = (500, 500)

HOUR: int = 60
MINUTE: int = 60

