
import sqlite3
from datetime import datetime


class DatabaseWriter:

    def __init__(self, *, database_connection: sqlite3.Connection) -> None:
        self.database_connection: sqlite3.Connection = database_connection
        self.cursor: sqlite3.Cursor = self.database_connection.cursor()
        self.current_date: str = self.__reformat_date()

    def insert_entry_to_database(self, *, worktime: str) -> None:

        """Wrapper method to be called to either insert or update an existing entry into or within the database.
        :param: worktime as a string
        :return: None"""

        if self._entry_exists_in_database():
            self.__update_existing_entry_in_database(worktime=worktime)

        else:
            self.__insert_new_entry_to_database(worktime=worktime)

        self.database_connection.commit()

    def __insert_new_entry_to_database(self, *, worktime: str) -> None:

        """
        Inserts a new worktime entry into the database, corresponding to the current date. Current date is used
        as the key for the worktime.
        :param worktime: overall worktime as a string to be stored within the database
        :return: None
        """
        self.cursor.execute(f"""INSERT INTO worktime_documentation (date,work_time) 
                                VALUES ('{self.current_date}','{worktime}')""")

    def __update_existing_entry_in_database(self, *, worktime: str) -> None:

        """
        Updates an existing worktime entry within the database, corresponding to the current date.
        :param worktime: overall worktime as a string to be stored within the database
        :return: None
        """
        self.cursor.execute(f"""UPDATE worktime_documentation
                                SET work_time = '{worktime}'
                                WHERE date = '{self.current_date}'
                                """)

    def _entry_exists_in_database(self) -> bool:

        """
        Checks whether an entry already exists within the given database connected to. Returns either true or false.
        """

        try:
            entry: str = self.cursor.execute(f"""SELECT * 
                                                 FROM worktime_documentation 
                                                 WHERE date='{self.current_date}'""").fetchone()

        except sqlite3.OperationalError as oe:
            print(f"Following error occurred while fetching data: {oe}")
            return False

        print(entry)

        return entry is not None

    def __reformat_date(self) -> str:

        """
        Grabs today's date and turns it into the right format to be used as key within the database. Returns the date
        as string in the right format.
        :return: today's date in the format required to be used within the database.
        """

        return datetime.now().strftime("%d-%m-%Y")
