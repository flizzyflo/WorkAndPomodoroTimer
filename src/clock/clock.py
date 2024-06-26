from typing import Self


class Clock:

    def __init__(self, *, initial_hours: int, initial_minutes: int, initial_seconds: int) -> None:
        self.hours: int = initial_hours
        self.minutes: int = initial_minutes
        self.seconds: int = initial_seconds

    def __add__(self, clock_object: Self) -> None:
        self.hours += clock_object.hours
        self.minutes += clock_object.minutes
        self.seconds += clock_object.seconds

    def __sub__(self, clock_object: Self) -> None:
        self.hours -= clock_object.hours
        self.minutes -= clock_object.minutes
        self.seconds -= clock_object.seconds

    def get_current_time(self) -> str:
        return f"{self.get_hours():02.0f}:{self.get_minutes():02.0f}:{self.get_seconds():02.0f}"

    def get_hours(self) -> int:
        return self.hours

    def get_minutes(self) -> int:
        return self.minutes

    def get_seconds(self) -> int:
        return self.seconds

    def set_hours_to(self, hours: int = 0) -> None:
        self.hours = hours

    def set_minutes_to(self, minutes: int = 0) -> None:
        self.minutes = minutes

    def set_seconds_to(self, seconds: int = 0) -> None:
        self.seconds = seconds

    def set_total_time(self, time: str) -> None:
        hours, minutes, seconds = time.split(":")
        self.set_hours_to(int(hours))
        self.set_minutes_to(int(minutes))
        self.set_seconds_to(int(seconds))

    def increase_seconds_by(self, seconds: int = 1) -> None:
        self.seconds += seconds

    def increase_minutes_by(self, minutes: int = 1) -> None:
        self.minutes += minutes

    def increase_hours_by(self, hours: int = 1) -> None:
        self.hours += hours

    def decrease_seconds_by(self, seconds: int = 1) -> None:
        self.seconds -= seconds

    def decrease_minutes_by(self, minutes: int = 1) -> None:
        self.minutes -= minutes

    def decrease_hours_by(self, hours: int = 1) -> None:
        self.hours -= hours

    def reset_clock(self) -> None:
        self.hours, self.minutes, self.seconds = 0, 0, 0
