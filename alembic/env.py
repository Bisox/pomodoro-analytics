import sys
from os.path import abspath, dirname

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Добавьте свой путь к проекту
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from config import settings  # Импортируйте настройки
from database.database import Base  # Импортируйте вашу базу данных

# Получение конфигурации Alembic
config = context.config

# Установка строки подключения из настроек
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

# Интерпретация файла конфигурации для Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Добавьте MetaData вашего модуля здесь
target_metadata = Base.metadata


# Двигатель конфигурации
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()