import sqlite3
import csv
from pathlib import Path
import os

# TODO add comments / docstring


class DatabaseReader:

    def __init__(self, *, database_connection: sqlite3.Connection):
        self.database_connection: sqlite3.Connection = database_connection
        self.cursor: sqlite3.Cursor = self.database_connection.cursor()

    def _read_database_entries(self) -> list:
        return self.cursor.execute("""SELECT * FROM worktime_documentation""").fetchall()

    def _export_database_entries(self, filepath: str | Path) -> None:
        all_database_entries: list = self._read_database_entries()
        export_file_path: Path = Path(os.path.join(filepath, "export.csv"))
        with open(os.path.join(export_file_path), "w") as exported_worktime_file:
            file = csv.writer(exported_worktime_file, delimiter=";")
            file.writerow(["date", "daily_work_time"])
            for entry in all_database_entries:
                file.writerow(entry)
