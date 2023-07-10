from src.clock.clock import Clock


class PomodoroClock(Clock):
    
    def __init__(self, *, minutes: int, seconds: int, break_time_short: int, break_time_long: int) -> None:
        super().__init__(initial_minutes=minutes, initial_seconds=seconds, initial_hours=0)
        self.break_count: int = 0
        self.break_time_short: int = break_time_short
        self.break_time_long: int = break_time_long
        self.next_break_time: int = 0
        self.is_active: bool = False

    def __repr__(self) -> str:
        return f"{self.get_minutes():02.0f}:{self.get_seconds():02.0f}"

    def pomodoro_is_active(self) -> bool:
        return self.is_active

    def set_pomodoro_active_to(self, *, active: bool) -> None:
        self.is_active = active
    
    def increase_break_counter_by(self, *, increase: int) -> None:
        self.break_count += increase

    def set_break_time(self) -> None:

        """Break-time depends on total count of breaks already taken."""

        if (self.get_break_counter() % 4 == 0) and (self.get_break_counter() != 0):
            self.next_break_time = self.get_break_time_long()

        else:
            self.next_break_time = self.get_break_time_short()

    def get_break_time_short(self) -> int:
        return self.break_time_short

    def get_break_time_long(self) -> int:
        return self.break_time_long

    def get_next_break_time(self) -> int:
        return self.next_break_time

    def get_break_counter(self) -> int:
        return self.break_count

    def reset_clock(self) -> None:
        super().reset_clock()
        self.increase_break_counter_by(increase=1)
        self.set_break_time()

    def reset_break_counter(self) -> None:
        self.break_count = 0

    def count_pomodoro_timer(self, seconds: int) -> None:
        """Checks minutes and seconds of the pomodoro counter. Increases break counter
        and manages clock counting in general."""
        
        if (self.get_minutes() == 0) & (self.get_seconds() == 0):
            self.reset_clock()
            self.set_pomodoro_active_to(active=False)

        elif self.get_seconds() == 0:
            self.decrease_minutes_by(minutes=1)
            self.set_seconds_to(seconds)
        
        else:
            self.decrease_seconds_by(seconds=1)
