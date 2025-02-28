import psycopg2
from psycopg2.extras import execute_values

class PostgresDB:
    def __init__(self, host, port, dbname, user, password):
        self.conn_params = {
            "host": host,
            "port": port,
            "dbname": dbname,
            "user": user,
            "password": password
        }
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(**self.conn_params)

    def insert_data(self, table_name, columns, data):
        if not data:
            return

        cols = ', '.join(columns)
        sql = f"INSERT INTO {table_name} ({cols}) VALUES %s"
        values = [tuple(row[col] for col in columns) for row in data]
        with self.conn.cursor() as cursor:
            execute_values(cursor, sql, values)
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
