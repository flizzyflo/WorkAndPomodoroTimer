class Clock:

    def __init__(self) -> None:
        self.hours, self.minutes, self.seconds = 0, 0, 0

    def getHours(self) -> int:
        return self.hours

    def getMinutes(self) -> int:
        return self.minutes

    def getSeconds(self) -> int:
        return self.seconds

    def setMinutes(self) -> None:
        self.minutes = 0

    def setSeconds(self) -> None:
        self.seconds = 0

    def increaseSeconds(self) -> None:
        self.seconds += 1

    def increaseMinutes(self) -> None:
        self.minutes += 1

    def increaseHours(self) -> None:
        self.hours += 1

    def resetClock(self) -> None:
        self.hours, self.minutes, self.seconds = 0, 0, 0

    def __repr__(self) -> str:
        return f"{self.getHours():02.0f}:{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"

