import sqlite3
from pathlib import Path
from src.database.database_writer import DatabaseWriter
from src.database.database_reader import DatabaseReader
from src.database.database_connector import DatabaseConnector


class DatabaseFacade:

    def __init__(self, *, database_path: str | Path) -> None:
        self.database_connection: sqlite3.Connection = DatabaseConnector.get_database_connection(database_path=database_path)
        self.database_writer: DatabaseWriter = DatabaseWriter(database_connection=self.database_connection)
        self.database_reader: DatabaseReader = DatabaseReader(database_connection=self.database_connection)

    def insert_data_into_database(self, worktime: str) -> None:
        self.database_writer.insert_entry_to_database(worktime=worktime)

    def entry_for_current_date_already_exists(self) -> bool:
        return self.database_writer._entry_exists_in_database()

    def export_database_entries(self, *, filepath: str | Path) -> None:
        return self.database_reader._export_database_entries(filepath=filepath)

    # TODO add menubar to select a path and start the export via button.
