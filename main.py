from database.sqlite_db import SQLiteDB
from database.pg_db import PostgresDB
from utils.logger import setup_logger
from utils.transfer import transfer_table
from config import settings

def main():
    logger = setup_logger()

    sqlite_db_path = settings.SQLITE_DB_PATH
    pg_config = settings.postgres_url

    # Инициализация подключений к БД
    sqlite_db = SQLiteDB(sqlite_db_path)
    sqlite_db.connect()
    logger.info("Подключение к SQLite выполнено.")

    pg_db = PostgresDB(
        pg_url=pg_config
    )
    pg_db.connect()
    logger.info("Подключение к PostgreSQL выполнено.")

    # Получение списка таблиц из SQLite и перенос данных
    tables = sqlite_db.get_tables()
    logger.info(f"Найдено таблиц: {tables}")

    for table in tables:
        try:
            transfer_table(sqlite_db, pg_db, table, logger)
        except Exception as e:
            logger.exception(f"Ошибка при переносе таблицы {table}: {e}")
            pg_db.session.rollback()

    sqlite_db.close()
    pg_db.close()
    logger.info("Перенос данных завершён.")

if __name__ == '__main__':
    main()
