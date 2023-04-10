
import datetime
import os
import sqlite3 as sl
from collections import namedtuple

from src.database.WorkTimeTuple import WorkTimeTuple
from src.settings.settings import EXPORT_HEADLINE, DATABASE_INFORMATION_FIELDS


class DatabaseManager:

    def __init__(self, database_name: str, table_name: str) -> None:
        
        self.table_name = table_name
        self.database_name = database_name
        self.connection = self.connect_to_database(self.database_name)
        self.cursor = self.connection.cursor()
        self.create_table(table_name)

    @staticmethod
    def entry_already_exists_in(*, database: 'DatabaseManager') -> bool:

        """Returns True if already a database entry for todays date exists."""

        year, month, day = str(datetime.date.today()).split("-")
        entry_exists = len(database.fetch_single_entry(year_filter=year, month_filter=month, day_filter=day).keys()) > 0

        return entry_exists

    def maintain_database_entry(self, date: datetime.date, duration: str) -> None:

        year, month, day = str(date).split("-")

        if len(self.fetch_single_entry(year, month, day)) > 0:
            self.__update_work_time_entry(year=year,
                                          month=month,
                                          day=day,
                                          duration=duration)
        
        else:
            self.__insert_work_time_duration(year=year,
                                             month=month,
                                             day=day,
                                             duration=duration)

        self.commit_work()

    def __update_work_time_entry(self, year: int, month: int, day: int, duration: str) -> None:

        """Updates an entry given within the database entry. Keys are the year, month and day."""

        if not self.connection:
            self.connection = self.connect_to_database(self.database_name)
    
        hours, minutes, seconds = duration.split(":")

        self.cursor.execute(f""" 
                            UPDATE {self.table_name} set hours= {hours}, minutes= {minutes}, seconds= {seconds} 
                            WHERE year == {year} 
                            AND month == {month} 
                            AND day == {day}
                            """)

    def __insert_work_time_duration(self, year: int, month: int, day: int, duration: str) -> None:

        """
        Duration format: 'hh:mm:ss' represents the work time of a specific day.
        Inserts the information into the database.
        """
        
        if not self.connection:
            self.connection = self.connect_to_database(self.database_name)

        hours, minutes, seconds = duration.split(":")
        
        self.cursor.execute(f""" 
                        INSERT INTO {self.table_name} (day, month, year, hours, minutes, seconds) 
                        VALUES ({day}, {month}, {year}, {hours}, {minutes}, {seconds})
                        """)

        self.connection.commit()

    def create_table(self, db_table_name: str) -> None:
        
        """
        Initially creates the work time-table within the database.
        """

        self.cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {db_table_name}
                        (day KEY varchar,
                        month KEY varchar,
                        year KEY varchar,
                        hours varchar,
                        minutes varchar,
                        seconds varchar,
                        description text)
                        """)

    def connect_to_database(self, database_name: str) -> sl.Connection:
        
        """
        Connects to the database to allow changing the data. Returns the connection object.
        """

        connection_to_database = sl.connect(database_name)
        return connection_to_database

    def fetch_single_entry(self, year_filter: int, month_filter: int, day_filter: int) -> dict[str, int | str]:
        
        """Gets a single entry from the database according to the input values given."""
        
        raw_fetch = self.connection.execute(f"""SELECT * 
                                            FROM {self.table_name} 
                                            WHERE year == {year_filter}
                                            AND month == {month_filter} 
                                            AND day == {day_filter}
                                            """).fetchall()[0]

        # maps values to field names and turns them into a dictionary
        field_value_dictionary = dict(zip(DATABASE_INFORMATION_FIELDS, raw_fetch))

        return field_value_dictionary

    def fetch_all_database_entries(self, year_filter: int = None, month_filter: int = None) -> list[tuple[str]]:
        
        """Gets all the information stored within the database."""
        
        if year_filter:
            return self.connection.execute(f"""SELECT * 
                                            FROM {self.table_name} 
                                            WHERE year == {year_filter}
                                            """).fetchall()
        
        elif month_filter:
            return self.connection.execute(f"""SELECT * 
                                            FROM {self.table_name} 
                                            WHERE month == {month_filter}
                                            """).fetchall()

        else:
            return self.connection.execute(f"""SELECT * 
                                            FROM {self.table_name} 
                                            """).fetchall()

    def save_csv_file_to_path(self, path: str) -> None:
        database_entries = self.fetch_all_database_entries()
        with open(os.path.join(path, "total_worktime_overview_export.csv"), "w") as exported_work_time_file:
            exported_work_time_file.write(EXPORT_HEADLINE)

            for row in database_entries:
                result = ""
                for column in row:
                    result += column + ";"
                
                result += "\n"

                exported_work_time_file.write(result)

    def commit_work(self) -> None:
        
        """Commits any work done on database level"""
        
        self.connection.commit()
