import os.path
import re
import sqlite3
from pathlib import Path
from typing import Tuple

from src.database.database_writer import DatabaseWriter
from src.database.database_reader import DatabaseReader
from src.database.database_connector import DatabaseConnector


class DatabaseFacade:

    """
    Facadeclass which has composition to all three different database working classes. This class is used to
    control the whole database behaviour from a single point of control.
    """
    def __init__(self) -> None:
        self.database_path = Path(os.path.join(os.path.dirname(__file__), "work_time.db"))
        self.database_connection: sqlite3.Connection = DatabaseConnector.get_database_connection(database_path=self.database_path)
        self.database_writer: DatabaseWriter = DatabaseWriter(database_connection=self.database_connection)
        self.database_reader: DatabaseReader = DatabaseReader(database_connection=self.database_connection)
        self.current_date: str = self.database_writer.get_current_date()

    def get_current_date(self) -> str:
        return self.current_date

    def insert_data_into_database(self, worktime: str) -> None:

        """
        Inserts new information about worktime into the database. Grabs the current date itself and
        combines it with the worktime to ensure the correct key-value combination. Calls method of class
        DatabaseWriter.
        :param worktime: Worktime as a string
        :return: None
        """

        self.database_writer.insert_entry_to_database(worktime=worktime)

    def grab_worktime_for(self, date_to_grab_for: str = None) -> str:

        regex_date_pattern: str = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(20[2-9][0-9])$"

        if date_to_grab_for is None:
            date_to_grab_for = self.current_date

        elif re.match(regex_date_pattern, date_to_grab_for) is None: # date is provided, but wrong format
            raise ValueError("Dateformat is wrong. Please provide date in format 'dd-mm-yyyy'")

        return self.database_reader._grab_worktime_for(date_to_grab_for=date_to_grab_for)

    def entry_for_current_date_already_exists(self) -> bool:

        """
        Checks whether an information for current date already stored within the database and returns a
        boolean value according to the evaluation. Current date is the key to check for duplicate.
        :return: True if value already exists in database, False otherwise
        """

        return self.database_writer._entry_exists_in_database()

    def export_database_entries(self, *, path_to_store_csv_file: str | Path, filename: str = "export.csv") -> None:

        """
        Method to store information to the users personal computer. Calls DatabaseReader class to call a method of
        it.
        :param path_to_store_csv_file: Path to store the exported file to
        :param filename: filename of the exported file. Per default is 'export.csv'
        :return: None
        """

        self.database_reader._export_database_entries(path_to_store_csv_file=path_to_store_csv_file,
                                                      filename=filename)

