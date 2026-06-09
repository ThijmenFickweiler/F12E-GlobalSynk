import sqlite3
from pathlib import Path

class database_conn:
    def __init__(self, database_location):
        self.database_connection = sqlite3.connect(Path(database_location))
        self.database_cursor = self.database_connection.cursor()

    def insert_data(self, columns, data, commit=True):
        self.database_cursor.execute(f"INSERT INTO product_index {columns} VALUES {data}")
        if commit:
            self.database_connection.commit()