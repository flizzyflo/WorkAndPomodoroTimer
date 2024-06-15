import os.path
import json
import os
from pathlib import Path


def read_from_json(filename: str) -> dict[str, int]:
    """
    Method  to read the contents of the json-file passed in as filename.
    Args:
        filename: filename of the json file to be read

    Returns:
        dict[str, str: returns the json content as a python dictionary

    """
    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))
    with open(settings_file_path, "r") as file_to_read:
        json_content = json.load(file_to_read)

    return json_content


def write_to_json(filename: str, content_to_write: dict[str, str]) -> None:
    """
    Method to write settings to the filename passed in as argument. Writes the dictionary content to the file.
    Args:
        filename: filename of the json settings file to write to
        content_to_write: dictionary storing the values to save to json file
    """
    settings_file_path: Path = Path(os.path.join(os.path.dirname(__file__), filename))
    j = json.dumps(content_to_write)

    with open(settings_file_path, "w") as file_to_write_to:
        file_to_write_to.write(j)

