# Первоначальная настройка

Сначала необходимо создать виртуальное окружение, а затем загрузить зависимости `pip install -r requirements.txt`

# Работа с БД

## Документация

- [SQLAlchemy быстрый старт](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) Официальная документация
- [Метанит SQL ORM SQLAlchemy](https://metanit.com/python/database/3.1.php) Есть устаревшая информация
- [Избыточный видеогайд](https://youtube.com/playlist?list=PLeLN0qH0-mCXARD_K-USF2wHctxzEVp40&si=b28Snxqbs87b12fB)Есть
  лишняя информация, но полезно для ознакомления

## Модели

### Базовая модель

Для начала создаётся базовая модель от которой в дальнейшем наследуются остальные модели

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): pass
```

### Модель

Модель представляет собой класс Python, который наследуется от базовой модели `Base`

Имя таблицы указывается через поле `__tablename__`

Тип данных поля указывается с помощью `Mapped[<тип>]`, если необходимы дополнительные ограничения, необходимо
использовать функцию `mapped_column` и передать в неё необходимые ограничения.

Например, первичный ключ `primary_key=True`

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase): pass


class ProductType(Base):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ratio: Mapped[float]
```

### Связи

Связь как и в любой реляционной БД осуществляется с помощью вторичных ключей
`ForeignKey("product_types.id", ondelete="CASCADE")`

Чтобы раскрыть всю крутость ORM и упростить доступ к типу продукта, SQLAlchemy предоставляет удобную функцию
`relationship`

Необходимо добавить поле для этого типа `type`, в качестве типа указывается его модель `Mapped["ProductType"]` и в итоге
приравнивается к результату функции `relationship()`

`type: Mapped["ProductType"] = relationship()`

Теперь можно запросить из БД продукты и для доступа например к имени продукта нам достаточно обратиться к полю
`type.name`, SQLAlchemy сама сделает дополнительный запрос в БД.

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase): pass


class ProductType(Base):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ratio: Mapped[float]


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id", ondelete="CASCADE"))
    type: Mapped["ProductType"] = relationship()
    name: Mapped[str]
    article: Mapped[int] = mapped_column(unique=True)
    min_cost: Mapped[float]
```

[Полный код моделей](database/models.py)

## Инициализация БД

### Создание движка

Для создания используется метод `create_engine(<database_url>)`, также можно указать параметр `echo=True` для вывода
всех обращений SQLAlchemy к БД

### Создание фабрики сессий для запросов к БД

Для создания используется метод `sessionmaker(bind=<движок>)`

### Первоначальное создание таблиц

Для создания таблиц необходимо обратиться к метаданным базовой модели и вызвать метод создания, передав движок.

Импорт внутри функции не просто так, это необходимо, чтобы избежать цикличного импорта, т.е. бесконечный цикл импортов
сначала файла `models.py` затем `database.py`

  ```python
def init_db():
    from database.models import Base

    Base.metadata.create_all(engine)
  ```

Для конфигурирования БД был создан простенький [файл](database/config.py)
`config.py`

В нём находится функция в которую подставляются необходимые значения

```python
LOGIN = "postgres"
PASSWORD = "1234"
DATABASE_NAME = "master_pol"


def get_database_url() -> str:
    return f"postgresql+psycopg://{LOGIN}:{PASSWORD}@localhost:5432/{DATABASE_NAME}"
```

Итоговый [файл](database/database.py):

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.config import get_database_url

engine = create_engine(get_database_url(), echo=True)
SessionFactory = sessionmaker(bind=engine)


def init_db():
    from database.models import Base
    Base.metadata.create_all(engine)
```

### Взаимодействия с БД

Поскольку были грамотно спроектированы модели, необходимо дописать свойство и 2 метода в классе `Partner`:

- `sales` свойство для получения продаж партнёра
- `save` метод для добавления и редактирования партнёра
- `get_all` статический метод для получения всех партнёров

```python
class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str]
    director: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str] = mapped_column(String(13))
    address: Mapped[str]
    inn: Mapped[str] = mapped_column(String(10))
    rate: Mapped[int]

    @property
    def sales(self):
        with SessionFactory() as session:
            return session.query(Sale).filter(Sale.partner == self).all()

    def save(self):
        with SessionFactory() as session:
            session.add(self)
            session.commit()

    @staticmethod
    def get_all():
        with SessionFactory() as session:
            return session.query(Partner).all()
```

### Запуск

Файл `main.py`:

```python
from database.database import init_db

if __name__ == '__main__':
    init_db()

```

### Заполнение БД и выгрузка SQL кода и ER-диаграммы

[Видео](https://drive.google.com/file/d/1RR_Cdjmx2C9cPuvdoC_s2gukE61hQxUX/view?usp=sharing) с нашего проекта, суть
осталась та же, таблицы только названием отличаются, в видео показаны возможные при импорте ошибки, так что
рекомендуется к просмотру.

# Интерфейс

## Документация

- [Официальная](https://habr.com/ru/articles/799203/)
- [Хабр](https://habr.com/ru/articles/799203/)

## Главное окно

Окно представляет собой класс наследуемый от `QMainWindow`

```python
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
```

## Создание виджетов

Все объекты интерфейса наследуются от `QWidget`

Для их проектирования используется утилита `QT Widgets Designer`. Для её запуска необходимо выполнить команду в
терминале `pyside6-designer`

После запуска утилиты необходимо выбрать шаблон виджета и нажать создать.

![Создание виджета](docs/img/create_widget.png)

### Страница партнёров

Затем переименовываем форму в окно партнёров

![Переименование окна](docs/img/rename_form.png)

### Компоновка

Интерфейс строится сверху вниз, поэтому:

- Добавляем в форму вертикальный слой
- `ПКМ по форме->Компоновка->Скомпоновать по вертикали`. Слой растянется по размеру формы.

  ![Компоновка](docs/img/vertical_layout.png)

### Заголовок

- Для центровки заголовка добавляем горизонтальный слой
- В него помещаем `Label`
- Задаём ему имя `pageTitle`

  ![Переименование заголовка](docs/img/rename_page_title.png)

- Устанавливаем горизонтальную и вертикальную политику в `Maximum`

  ![Заголовок](docs/img/page_title_position.png)

### Зона с партнёрами

- Под слой заголовка добавляем `Scroll Area`, под лой заголовка. Она автоматически займёт большую область страницы

  ![Добавления зоны партнёров](docs/img/add_scroll_area.png)

- Меняем имя на `partnersArea`

  ![Переименование зоны партнёров](docs/img/rename_scroll_area.png)

### Добавляем в проект

- Сохраняем страницу в директорию `ui`
- Конвертируем в python класс командой `pyside6-uic ui/partners_page.ui -o ui/ui_partners_page.py`
- Создаём класс `PartnersPage` и наследуем его от сгенерируемого класса
- В конструкторе вызываем функцию `setupUi`
- И устанавливаем текст заголовка

```python
from PySide6.QtWidgets import QWidget

from ui.ui_partners_page import Ui_partnersPage


class PartnersPage(QWidget, Ui_partnersPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageTitle.setText("Страница партнёров")
```

## Запуск приложения

Инициализация интерфейса перед запуском происходит в [файле](ui/app.py) `app.py`

- Создаём единственный экземпляр класса приложения `QApplication` и передаём в него аргументы `sys.argv` при запуске,
  они представляют список, поэтому можно передать пустой список `QApplication([])`
    - Задаём иконку приложению с помощью метода `setWindowIcon`, в неё передаём объект класса `QIcon`, которому передаём
      путь до иконки
- Создаём главное окно
    - Настраиваем ему минимальный размер, значения подбираем, чтобы интерфейс не перекрывался
    - Задаём заголовок
    - Создаём виджет страницы партёров `PartnersPage` и устанавливаем его центральным с помощью метода
      `setCentralWidget`
    - Отображаем окно методом `show`
- Запускаем приложение `sys.exit(app.exec())`

```python
import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from ui.main_window import MainWindow
from ui.partners_page import PartnersPage


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/icons/master_pol.ico'))

    main_window = MainWindow()
    main_window.setMinimumSize(500, 250)
    main_window.setWindowTitle('Мастер пол')
    partners_page = PartnersPage()
    main_window.setCentralWidget(partners_page)
    main_window.show()

    sys.exit(app.exec())
```

- Добавляем вызов функции `run_app` в [файл](main.py) `main.py`

```python
from database.database import init_db
from ui.app import run_app

if __name__ == '__main__':
    init_db()
    run_app()
```