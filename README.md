# SQLBridge

![Static Badge](https://img.shields.io/badge/Python-3.11-blue)
![Static Badge](https://img.shields.io/badge/psycopg2-2.9.10-blue)
![Static Badge](https://img.shields.io/badge/SQLAlchemy-2.0.38-blue)

**SQLBridge** — это инструмент для автоматизированного переноса данных из базы данных SQLite в PostgreSQL. Приложение
сканирует все таблицы в SQLite, считывает их структуру и данные, а затем переносит их в заранее подготовленные таблицы
PostgreSQL.

---

## Особенности

- **Автоматизация:** Приложение автоматически сканирует таблицы SQLite и переносит данные в PostgreSQL при запуске.
- **Логирование:** Подробное логирование всех операций помогает отслеживать процесс миграции и выявлять ошибки.
- **Конфигурируемость:** Все параметры подключения к базам данных задаются через файл `.env`.


# ВНИМАНИЕ
⚠️Перед запуском убедитесь что в базе данных PostgreSQL созданы таблицы с такими же названиями таблиц, 
названиями столбцов и параметрами столбцов как и в SQLITE!!!

---

## Требования

- **Python:** версия 3.8 и выше.
- **SQLite:** стандартный модуль `sqlite3` (входит в стандартную библиотеку Python).
- **PostgreSQL:** сервер PostgreSQL.
- **Библиотека для PostgreSQL:** [psycopg2-binary](https://www.psycopg.org/)  
  
## Структура проекта

```psql
    SQLBridge/
    │
    ├── config.py           # Файл конфигурации для подключения к БД
    ├── main.py             # Основной скрипт приложения
    ├── db/
    │   ├── __init__.py     # Инициализация пакета для работы с БД
    │   ├── sqlite_db.py    # Модуль для работы с SQLite
    │   └── pg_db.py        # Модуль для работы с PostgreSQL
    └── utils/
        ├── __init__.py     # Инициализация пакета утилит
        ├── logger.py       # Модуль для настройки логирования
        └── transfer.py     # Модуль, реализующий логику переноса данных
```

## Установка и настройка

1. ### Клонирование репозитория:
   ```bash
   git clone https://github.com/IPRepin/SQLBridge.git
   cd project
2. ### Создание виртуального окружения:
   #### Для Linux/Mac:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
   #### Для Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
3. ### Установка зависимостей:
    ```bash
    pip install -r requirements.txt  # Если есть файл requirements.txt
   ```
4. ### Настройка файла конфигурации:
    ```ini
    [sqlite]
    SQLITE_DB_PATH=path_your_sqlite_database
    
    [postgres]
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432 #your local postgres host(default 5432)
    POSTGRES_DB=your_local_db_name
    POSTGRES_USER=your_local_postgres_user
    POSTGRES_PASSWORD=your_local_postgres_password
    
    LOG_LEVEL=level_logging(INFO)
    ```
## Запуск приложения
```bash
python main.py
```
Приложение выполнит:
1. Подключение к базе данных SQLite.
2. Получение списка таблиц и информации о колонках.
3. Перенос данных в соответствующие таблицы PostgreSQL.
4. Вывод логов операций в консоль.

## Автоматический запуск
* Cron (Linux) : Добавьте задание в crontab для периодического запуска.
* Systemd (Linux) : Создайте unit-файл для сервиса.
* Task Scheduler (Windows) : Настройте задачу через Планировщик задач.
## Логирование
Логирование настроено через модуль logging в файле utils/logger.py. Информационные и ошибочные сообщения выводятся в консоль. Настройки можно изменить в данном модуле.

## Обработка ошибок
* Для каждой таблицы реализована обработка исключений.
* При возникновении ошибки она логируется, а приложение продолжает работу с другими таблицами.

## Лицензия
Проект распространяется под лицензией MIT. Подробности в файле LICENSE.txt