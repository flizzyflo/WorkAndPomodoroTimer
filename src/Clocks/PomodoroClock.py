# from Settings.Settings import 

class PomodoroClock:
    
    def __init__(self, minutes: int, seconds: int, breaktimeShort: int, breaktimeLong: int) -> None:
        self.minutes: int = minutes
        self.seconds: int = seconds
        self.breakCounter: int = 0
        self.breakTimeShort: int = breaktimeShort
        self.breakTimeLong: int = breaktimeLong
        self.pomodoroActive: bool = False

    def __repr__(self) -> str:
        return f"{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"


    def setPomodoroActive(self, active: bool) -> None:
        self.pomodoroActive = active
    

    def getPomodoroActive(self) -> bool:
        return self.pomodoroActive


    def increaseBreakCounter(self) -> None:
        self.breakCounter += 1


    def decreaseMinutes(self) -> None:
        self.minutes -= 1


    def decreaseSeconds(self) -> None:
        self.seconds -= 1


    def setMinutes(self, minutes: int) -> None:
        self.minutes = minutes


    def setSeconds(self, seconds: int) -> None:
        self.seconds = seconds


    def getMinutes(self) -> int:
        return self.minutes


    def getSeconds(self) -> int:
        return self.seconds


    def setBreakTime(self, breakTimeLong: int, breakTimeShort: int) -> None:
        
        if self.getBreakCounter() % 4 == 0 and (self.getBreakCounter() != 0):
            self.breakTimeShort = breakTimeLong

        else:
            self.breakTimeShort = breakTimeShort 


    def getBreakTime(self) -> int:
        return self.breakTimeShort


    def getBreakCounter(self) -> int:
        return self.breakCounter


    def resetClock(self, minutes: int, seconds: int) -> None:
        self.minutes, self.seconds = minutes, seconds
        self.increaseBreakCounter()
        self.setBreakTime(self.breakTimeLong, self.breakTimeShort)


    def resetBreakCounter(self) -> None:
        self.breakCounter = 0


    def countPomodoroTimer(self, seconds: int) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""
        
        if (self.getMinutes() == 0) & (self.getSeconds() == 0):
            self.resetClock(minutes= self.getMinutes(), seconds= self.getSeconds())
            self.setPomodoroActive(False)

        
        elif self.getSeconds() == 0:
            self.decreaseMinutes()
            self.setSeconds(seconds)
        
        else:
            self.decreaseSeconds()