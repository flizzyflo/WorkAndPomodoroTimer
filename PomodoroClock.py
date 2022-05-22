class PomodoroClock:
    
    def __init__(self) -> None:
        self.minutes: int = 24
        self.seconds: int = 60
        self.breakCounter: int = 0
        self.breakTime: int = 5
        self.pomodoroActive: bool = False

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
        
        if self.getBreakCounter() == 4:
            self.breakTime = breakTimeLong

        else:
            self.breakTime = breakTimeShort 

    def getBreakTime(self) -> int:
        return self.breakTime

    def getBreakCounter(self) -> int:
        return self.breakCounter

    def resetClock(self, minutes: int, seconds: int) -> None:
        self.minutes, self.seconds = minutes, seconds

    def resetBreakCounter(self) -> None:
        self.breakCounter = 0

    def __repr__(self) -> str:
        return f"{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"