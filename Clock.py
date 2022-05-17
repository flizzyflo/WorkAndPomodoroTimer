class Clock:

    def __init__(self):
        self.hours, self.minutes, self.seconds = 0, 0, 0

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def setMinutes(self):
        self.minutes = 0

    def setSeconds(self):
        self.seconds = 0

    def increaseSeconds(self):
        self.seconds += 1

    def increaseMinutes(self):
        self.minutes += 1

    def increaseHours(self):
        self.hours += 1

    def resetClock(self):
        self.hours, self.minutes, self.seconds = 0, 0, 0

    def __repr__(self):
        return f"{self.getHours():02.0f}:{self.getMinutes():02.0f}:{self.getSeconds():02.0f}"

