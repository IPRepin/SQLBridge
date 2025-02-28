def transfer_table(sqlite_db, pg_db, table_name, logger):
    logger.info(f"Начинаем перенос таблицы {table_name}")
    columns = sqlite_db.get_table_columns(table_name)
    logger.info(f"Колонки: {columns}")
    data = sqlite_db.fetch_all_data(table_name)
    if data:
        pg_db.insert_data(table_name, columns, data)
        logger.info(f"Перенос данных таблицы {table_name} завершён. Всего записей: {len(data)}")
    else:
        logger.info(f"Таблица {table_name} пуста, пропускаем.")
