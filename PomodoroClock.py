class PomodoroClock:
    
    def __init__(self) -> None:
        self.minutes: int = 24
        self.seconds: int = 60
        self.pomodoroTime: int = 25
        self.breakCounter: int = 0
        self.breakTime: int = 5

    def increaseBreakCounter(self) -> None:
        self.breakCounter += 1

    def decreaseMinutes(self) -> None:
        self.minutes -= 1

    def decreaseSeconds(self) -> None:
        self.seconds -= 1

    def setMinutes(self) -> None:
        self.minutes = 24

    def setSeconds(self) -> None:
        self.seconds = 60

    def getMinutes(self) -> int:
        return self.minutes

    def getSeconds(self) -> int:
        return self.seconds

    def setBreakTime(self) -> None:
        
        if self.getBreakCounter() == 4:
            self.breakTime = 20

        else:
            self.breakTime = 5 

    def getBreakTime(self) -> int:
        return self.breakTime

    def getBreakCounter(self) -> int:
        return self.breakCounter

    def resetClock(self) -> None:
        self.minutes, self.seconds = 0, 0

    def resetBreakCounter(self) -> None:
        self.breakCounter = 0

    def __repr__(self) -> str:
        return f"{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"