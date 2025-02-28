from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker


class PostgresDB:
    def __init__(self, pg_url):
        self.connection_string = str(pg_url)
        self.engine = create_engine(self.connection_string)
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def connect(self):
        self.session = self.Session()

    def reflect_table(self, table_name):
        table_name = table_name.lower()
        return Table(table_name, self.metadata, autoload_with=self.engine)

    def insert_data(self, table_name, columns, data):
        table = self.reflect_table(table_name)
        # Получаем список столбцов, определённых в целевой таблице
        target_columns = table.columns.keys()
        # Фильтруем колонки, оставляя только те, что есть в обеих БД
        common_columns = [col for col in columns if col in target_columns]
        # Формируем список словарей для вставки, используя только общие колонки
        data_dicts = [{col: row[col] for col in common_columns} for row in data]
        stmt = insert(table).values(data_dicts)
        # Обновляем записи при конфликте (кроме первичного ключа 'id')
        update_dict = {col: stmt.excluded[col] for col in common_columns if col != 'id'}
        stmt = stmt.on_conflict_do_update(
            index_elements=['id'],
            set_=update_dict
        )
        self.session.execute(stmt)
        self.session.commit()

    def close(self):
        if self.session:
            self.session.close()
