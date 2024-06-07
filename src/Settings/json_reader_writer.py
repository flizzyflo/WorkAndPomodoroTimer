import os.path
import json
import os
from pathlib import Path


def read_from_json(filename: str) -> dict[str, int]:
    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))
    with open(settings_file_path, "r") as file_to_read:
        json_content = json.load(file_to_read)

    return json_content


def write_to_json(filename: str, content_to_write: dict[str, str]) -> None:
    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))
    j = json.dumps(content_to_write)

    with open(settings_file_path, "w") as file_to_write_to:
        file_to_write_to.write(j)

