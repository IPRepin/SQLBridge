import sqlite3

class SQLiteDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def get_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row['name'] for row in cursor.fetchall() if row['name'] != 'sqlite_sequence']
        return tables

    def get_table_columns(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [row['name'] for row in cursor.fetchall()]
        return columns

    def fetch_all_data(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        return rows

    def close(self):
        if self.conn:
            self.conn.close()
