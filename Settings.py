from random import randint

fontDict = ('calibri', 25, 'bold')
width = 30
frameSize = "500x500"

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

LONGBREAK = 20
SHORTBREAK = 5
POMODOROMINUTES = 24
POMODOROSECONDS = 60

def returnRandomBreakMessage(pomodoroObject: object):

    messages = [f"You should take a break. Your break should last {pomodoroObject.getBreakTime()} minutes. After that, you will be even more productive, I promise!",
                f"Nothing moves us forward on our journey better than a break. Enjoy your {pomodoroObject.getBreakTime()} minutes!",
                f"Calmness attracts life, restlessness scares it away. Be calm for at least {pomodoroObject.getBreakTime()} minutes.",
                f"We have far too little leisure: time when nothing is going on. This is the time when the Einsteins, the creative researchers, make their discoveries. The business and the routine are uninteresting and counterproductive. Take a break for {pomodoroObject.getBreakTime()} minutes.",
                f"What happens without rests does not last. Rest for {pomodoroObject.getBreakTime()} minutes.",
                ]

    return messages[randint(0, len(messages) - 1)]
