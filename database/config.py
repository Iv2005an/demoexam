LOGIN = "postgres"
PASSWORD = "1234"
DATABASE_NAME = "master_pol"


def get_database_url() -> str:
    return f"postgresql+psycopg://{LOGIN}:{PASSWORD}@localhost:5432/{DATABASE_NAME}"
