import tkinter as tk
from typing import Dict, List

from ..settings.json_reader_writer import read_from_json, write_to_json
from ..settings.settings import BUTTON_STYLE, ENTRY_WIDTH, LABEL_WIDTH, PADY, PADX, SETTING_TIME_LABEL_NAMES


class SettingsMenu(tk.Tk):
    normal_worktime_hours: tk.Entry
    normal_worktime_minutes: tk.Entry
    normal_worktime_seconds: tk.Entry
    max_worktime_hours: tk.Entry
    max_worktime_minutes: tk.Entry
    max_worktime_seconds: tk.Entry
    button_frame: tk.Frame
    label_frame: tk.Frame
    entry_frame: tk.Frame
    save_button: tk.Button
    quit_button: tk.Button
    work_time_settings: Dict[str, str]
    label_names: List[str]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Work-Time Settings")
        self.attributes("-topmost", True)
        self.label_frame = tk.Frame(master=self)
        self.label_frame.grid(column=0, row=0)
        self.entry_frame = tk.Frame(master=self)
        self.entry_frame.grid(column=1, row=0, padx=PADX, pady=PADY)
        self.button_frame = tk.Frame(master=self)
        self.button_frame.grid(column=0, row=1, columnspan=2, padx=PADX, pady=PADY)
        self.label_names = SETTING_TIME_LABEL_NAMES
        self.save_button = None
        self.quit_button = None
        self.normal_worktime_hours = None
        self.normal_worktime_minutes = None
        self.max_worktime_hours = None
        self.max_worktime_minutes = None
        self.initialize_label_widgets()
        self.initialize_entry_widgets()
        self.initialize_button_widgets()

    def initialize_button_widgets(self) -> None:
        self.save_button = tk.Button(master=self.button_frame,
                                     text="Save",
                                     command=lambda: self.save_settings(),
                                     **BUTTON_STYLE)
        self.save_button.pack(fill=tk.BOTH)
        self.quit_button = tk.Button(master=self.button_frame,
                                     text="Quit",
                                     command=lambda: self.quit_settings_menu(),
                                     **BUTTON_STYLE)
        self.quit_button.pack(fill=tk.BOTH)

    def initialize_label_widgets(self) -> None:
        for row, label_text in enumerate(self.label_names):
            tk.Label(master=self.entry_frame,
                     text=label_text,
                     anchor="e",
                     justify="right",
                     width=LABEL_WIDTH).grid(column=0, row=row)

    def initialize_entry_widgets(self) -> None:
        work_time_settings = read_from_json("work_times.json")

        self.normal_worktime_hours = tk.Entry(master=self.entry_frame,
                                              width=ENTRY_WIDTH,
                                              justify="center")
        self.normal_worktime_hours.insert(0, str(work_time_settings["NORMAL_DAILY_WORK_TIME_HOURS"]))
        self.normal_worktime_hours.grid(column=1, row=0)

        self.normal_worktime_minutes = tk.Entry(master=self.entry_frame,
                                                width=ENTRY_WIDTH,
                                                justify="center")
        self.normal_worktime_minutes.insert(0, str(work_time_settings["NORMAL_DAILY_WORK_TIME_MINUTES"]))
        self.normal_worktime_minutes.grid(column=1, row=1)

        self.max_worktime_hours = tk.Entry(master=self.entry_frame,
                                           width=ENTRY_WIDTH,
                                           justify="center")
        self.max_worktime_hours.insert(0, str(work_time_settings["MAX_DAILY_WORK_TIME_HOURS"]))
        self.max_worktime_hours.grid(column=1, row=2)

        self.max_worktime_minutes = tk.Entry(master=self.entry_frame,
                                             width=ENTRY_WIDTH,
                                             justify="center")
        self.max_worktime_minutes.insert(0, str(work_time_settings["MAX_DAILY_WORK_TIME_MINUTES"]))
        self.max_worktime_minutes.grid(column=1, row=3)

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
        self.quit_settings_menu()

    def quit_settings_menu(self) -> None:
        self.destroy()