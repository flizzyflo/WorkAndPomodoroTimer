class Clock:

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def __repr__(self) -> str:
        return f"{self.getHours():02.0f}:{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"


    def __add__(self, object: object) -> None:
        self.hours += object.hours
        self.minutes += object.minutes
        self.seconds += object.seconds


    def __sub__(self, object: object) -> None:
        self.hours -= object.hours
        self.minutes -= object.minutes
        self.seconds -= object.seconds


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

    def decreaseSeconds(self) -> None:
        self.seconds -= 1

    def decreaseMinutes(self) -> None:
        self.minutes -= 1

    def decreaseHours(self) -> None:
        self.hours -= 1

    def resetClock(self) -> None:
        self.hours, self.minutes, self.seconds = 0, 0, 0

    def countTime(self) -> None:
        """Main method to count and get information of the work time clock object
        about the work time itself."""

        if self.getSeconds() == 60:
            self.increaseMinutes()
            self.setSeconds()

        else:
            self.increaseSeconds()

        if self.getMinutes() == 60:
            self.increaseHours()
            self.setMinutes()

