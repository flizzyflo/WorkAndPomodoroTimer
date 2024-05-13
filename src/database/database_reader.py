import sqlite3
import csv
from pathlib import Path
import os
import re
from typing import Tuple, List


class DatabaseReader:

    """
    Class to read information from the database as well as exporting these information to
    the users personal computer as a csv file.
    """

    def __init__(self, *, database_connection: sqlite3.Connection):
        self.database_connection: sqlite3.Connection = database_connection
        self.cursor: sqlite3.Cursor = self.database_connection.cursor()

    def _grab_worktime_for(self, *, date_to_grab_for: str) -> Tuple[str]:

        """
        Grabs the worktime stored for the specific date passed in as argument and returns it as a string.
        :param date_to_grab_for: date needed to grab the value. Format is dd-mm-yyyy
        :return: worktime for the date_to_grab_for in format hh:mm:ss
        """

        return self.cursor.execute(f"""SELECT work_time 
                                       FROM worktime_documentation 
                                       WHERE date = '{date_to_grab_for}'""").fetchone()[0] # to return just the tuple without the surrounding list

    def _read_database_entries(self) -> List[str]:

        """Fetches all entries from the database table where the worktime information are stored. Returns a
        list of tuples containing the information about date and worktime.
        :return: list[tuple[str, str]] - A tuple looks like this: (17-07-2023, 07:48:00), being (date, worktime)"""

        return self.cursor.execute("""SELECT * FROM worktime_documentation""").fetchall()

    def _export_database_entries(self, path_to_store_csv_file: str | Path, filename: str) -> None:

        """
        Method to export the data stored within the database and store the data into a csv file with two columns
        date; worktime.
        :param path_to_store_csv_file: filepath where csv file should be stored at.
        :param filename: filename of the exported csv file which stores the database information. Is export.csv per default.
        :return: None
        """

        all_database_entries: list = self._read_database_entries()
        export_file_path: Path = Path(os.path.join(path_to_store_csv_file, filename))
        with open(os.path.join(export_file_path), "w") as exported_worktime_file:
            file = csv.writer(exported_worktime_file, delimiter=";")
            file.writerow(["date", "daily_work_time"])
            for entry in all_database_entries:
                file.writerow(entry)
