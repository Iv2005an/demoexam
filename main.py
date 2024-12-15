from database.database import init_db
from ui.app import run_app

if __name__ == '__main__':
    init_db()
    run_app()
