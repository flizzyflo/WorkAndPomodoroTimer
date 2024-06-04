import tkinter as tk
from typing import Dict

from ..settings.work_time_barriers import read_from_json, write_to_json


class SettingsMenu(tk.Tk):
    normal_worktime_hours: tk.Entry
    normal_worktime_minutes: tk.Entry
    normal_worktime_seconds: tk.Entry
    max_worktime_hours: tk.Entry
    max_worktime_minutes: tk.Entry
    max_worktime_seconds: tk.Entry
    entry_frame: tk.Frame
    work_time_settings: Dict[str, str]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.entry_frame = tk.Frame(master=self)
        self.entry_frame.pack()
        self.initialize_entry_widgets()

        self.save_button = tk.Button(master=self, text="Save", command=lambda: self.save_settings())
        self.save_button.pack(fill=tk.BOTH)
        self.quit_button = tk.Button(master=self, text="Quit", command=lambda: self.destroy())
        self.quit_button.pack(fill=tk.BOTH)

    def initialize_entry_widgets(self) -> None:
        work_time_settings = read_from_json("work_times.json")
        print(work_time_settings)
        tk.Label(master=self.entry_frame, text="Usual daily hours: ").grid(column=0, row=0)
        self.normal_worktime_hours = tk.Entry(master=self.entry_frame)
        self.normal_worktime_hours.insert(0, str(work_time_settings["NORMAL_DAILY_WORK_TIME_HOURS"]))
        self.normal_worktime_hours.grid(column=1, row=0)

        tk.Label(master=self.entry_frame, text="Usual daily minutes: ").grid(column=0, row=1)
        self.normal_worktime_minutes = tk.Entry(master=self.entry_frame)
        self.normal_worktime_minutes.insert(0, str(work_time_settings["NORMAL_DAILY_WORK_TIME_MINUTES"]))
        self.normal_worktime_minutes.grid(column=1, row=1)

        tk.Label(master=self.entry_frame, text="Max daily hours: ").grid(column=0, row=3)
        self.max_worktime_hours = tk.Entry(master=self.entry_frame)
        self.max_worktime_hours.insert(0, str(work_time_settings["MAX_DAILY_WORK_TIME_HOURS"]))
        self.max_worktime_hours.grid(column=1, row=3)

        tk.Label(master=self.entry_frame, text="Max daily minutes: ").grid(column=0, row=4)
        self.max_worktime_minutes = tk.Entry(master=self.entry_frame)
        self.max_worktime_minutes.insert(0, str(work_time_settings["MAX_DAILY_WORK_TIME_MINUTES"]))
        self.max_worktime_minutes.grid(column=1, row=4)

    def save_settings(self) -> None:
        new_settings = {
            "NORMAL_DAILY_WORK_TIME_HOURS": self.normal_worktime_hours.get(),
            "NORMAL_DAILY_WORK_TIME_MINUTES": self.normal_worktime_minutes.get(),
            "NORMAL_DAILY_WORK_TIME_SECONDS": 0,
            "MAX_DAILY_WORK_TIME_HOURS": self.max_worktime_hours.get(),
            "MAX_DAILY_WORK_TIME_MINUTES": self.max_worktime_minutes.get(),
            "MAX_DAILY_WORK_TIME_SECONDS": 0
        }

        write_to_json("work_times.json", new_settings)
        self.destroy()