import sqlite3
import os
from pathlib import Path


class DatabaseConnector:

    """
    Factory class to return the connection for the specific database desired.
    """

    @staticmethod
    def get_database_connection(*, database_path: str | Path) -> sqlite3.Connection:

        """
        Connects to the database and returns the Connection object to the database to work with later on.
        Checks path existence and raises an error if path does not exist.
        :param database_path: filepath where the specific database is located
        :raises FileNotFoundError: if path to database passed in as argument does not exist
        :return: sqlite3.Connection object to the database passed in as path
        """

        if not DatabaseConnector.path_exists(path=database_path):
            raise FileNotFoundError

        return sqlite3.connect(database=database_path)

    @staticmethod
    def path_exists(*, path: str | Path) -> bool:
        """
        Checks the existence of a path passed in as an argument. Returns either true or false
        """
        return os.path.exists(path)

    @staticmethod
    def create_database(*, database_path: str | Path, database_name: str) -> None:

        if not DatabaseConnector.path_exists(path=database_path):
            raise FileNotFoundError

        full_database_path: str = str(os.path.join(database_path, database_name))
        if not full_database_path.endswith(".db"):
            full_database_path: Path = Path(full_database_path + ".db")

        sqlite3.connect(database=full_database_path)

    @staticmethod
    def create_database_table(database_path: str | Path) -> None:
        cursor: sqlite3.Cursor = DatabaseConnector.get_database_connection(database_path=database_path).cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS worktime_documentation
          ([date] date PRIMARY KEY, [work_time] TEXT)
        """)

