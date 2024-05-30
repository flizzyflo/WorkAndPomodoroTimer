
import tkinter as tk
from ..settings.work_time_barriers import read_from_json, write_to_json


class SettingsMenu(tk.Tk):
    normal_worktime_hours: tk.Entry
    normal_worktime_minutes: tk.Entry
    normal_worktime_seconds: tk.Entry
    max_worktime_hours: tk.Entry
    max_worktime_minutes: tk.Entry
    max_worktime_seconds: tk.Entry
    entry_frame: tk.Frame

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.entry_frame = tk.Frame(master= self)
        self.entry_frame.pack()
        self.initialize_entry_widgets()

        self.save_button = tk.Button(master=self, text="Save", command=lambda: quit())
        self.save_button.pack()
        self.quit_button = tk.Button(master=self, text="Quit", command=lambda: quit())
        self.quit_button.pack()



    def initialize_entry_widgets(self) -> None:
        r = read_from_json("work_times.json")
        self.normal_worktime_hours = tk.Entry(master=self.entry_frame)
        self.normal_worktime_hours.insert(0, str(r["NORMAL_DAILY_WORK_TIME_HOURS"]))
        self.normal_worktime_hours.pack()

        self.normal_worktime_minutes = tk.Entry(master=self.entry_frame)
        self.normal_worktime_minutes.insert(0, str(r["NORMAL_DAILY_WORK_TIME_MINUTES"]))
        self.normal_worktime_minutes.pack()

        self.normal_worktime_seconds = tk.Entry(master=self.entry_frame)
        self.normal_worktime_seconds.insert(0, str(r["NORMAL_DAILY_WORK_TIME_SECONDS"]))
        self.normal_worktime_seconds.pack()

        self.max_worktime_hours = tk.Entry(master=self.entry_frame)
        self.max_worktime_hours.insert(0, str(r["MAX_DAILY_WORK_TIME_HOURS"]))
        self.max_worktime_hours.pack()

        self.max_worktime_minutes = tk.Entry(master=self.entry_frame)
        self.normal_worktime_hours.insert(0, str(r["MAX_DAILY_WORK_TIME_MINUTES"]))
        self.normal_worktime_hours.pack()

        self.max_worktime_seconds = tk.Entry(master=self.entry_frame)
        self.max_worktime_seconds.insert(0, str(r["MAX_DAILY_WORK_TIME_SECONDS"]))
        self.max_worktime_seconds.pack()

