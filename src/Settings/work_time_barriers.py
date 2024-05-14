import os.path
from enum import Enum
import json
import os
from pathlib import Path


def read_from_json(filename: str) -> dict[str, int]:

    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))
    with open(settings_file_path, "r") as file_to_read:
        json_content = json.load(file_to_read)

    return json_content


def write_to_json(filename: str) -> None:
    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))


class WorkTimeBarriers(Enum):

    """
    work time barriers
    """

    work_time_settings = read_from_json("work_times.json")

    NORMAL_DAILY_WORK_TIME_HOURS: int = work_time_settings["NORMAL_DAILY_WORK_TIME_HOURS"]
    NORMAL_DAILY_WORK_TIME_MINUTES: int = work_time_settings["NORMAL_DAILY_WORK_TIME_MINUTES"]
    NORMAL_DAILY_WORK_TIME_SECONDS: int = work_time_settings["NORMAL_DAILY_WORK_TIME_SECONDS"]
    MAX_DAILY_WORK_TIME_HOURS: int = work_time_settings["MAX_DAILY_WORK_TIME_HOURS"]
    MAX_DAILY_WORK_TIME_MINUTES: int = work_time_settings["MAX_DAILY_WORK_TIME_MINUTES"]
    MAX_DAILY_WORK_TIME_SECONDS: int = work_time_settings["MAX_DAILY_WORK_TIME_SECONDS"]
