import sqlite3
import os
from pathlib import Path


class DatabaseConnector:
    """
    Factory class to return the connection for the specific database desired.
    """

    @staticmethod
    def get_database_connection(*, database_path: Path) -> sqlite3.Connection:

        """
        Connects to the database and returns the Connection object to the database to work with later on.
        Checks path existence and raises an error if path does not exist.
        :param database_path: filepath where the specific database is located
        :raises FileNotFoundError: if path to database passed in as argument does not exist
        :return: sqlite3.Connection object to the database passed in as path
        """

        db_connection: sqlite3.Connection

        if not database_path.exists():
            db_connection = sqlite3.connect(database=database_path)
            DatabaseConnector.create_database_table(database_path=database_path)
        else:
            db_connection = sqlite3.connect(database=database_path)

        return db_connection

    @staticmethod
    def path_exists(*, path: str | Path) -> bool:
        """
        Checks the existence of a path passed in as an argument. Returns either true or false
        """
        return os.path.exists(path)

    @staticmethod
    def create_database_table(database_path: str | Path) -> None:
        cursor: sqlite3.Cursor = DatabaseConnector.get_database_connection(database_path=database_path).cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS worktime_documentation
            ([date] date PRIMARY KEY, 
            [work_time] TEXT)
            """)

        cursor.close()
