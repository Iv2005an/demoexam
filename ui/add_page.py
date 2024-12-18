from PySide6.QtWidgets import QWidget, QMainWindow

from database.models import Partner
from ui.ui_add_page import Ui_addPage


class AddPage(QWidget, Ui_addPage):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.nameTitle.setText("Наименование:")
        self.typeTitle.setText("Тип:")
        self.typeField.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        self.innTitle.setText("ИНН:")
        self.rateTitle.setText("Рейтинг:")
        self.addressTitle.setText("Адрес:")
        self.directorTitle.setText("Директор:")
        self.phoneTitle.setText("Телефон:")
        self.emailTitle.setText("Почта:")
        self.addButton.setText("Добавить")
        self.addButton.clicked.connect(self.add)
        self.cancelButton.setText("Отмена")
        self.cancelButton.clicked.connect(self.cancel)

    def add(self):
        partner = Partner(
            name=self.nameField.text(),
            type=self.typeField.currentText(),
            inn=self.innField.text(),
            rate=self.rateField.text(),
            address=self.addressField.text(),
            director=self.directorFiled.text(),
            phone=self.phoneField.text(),
            email=self.emailField.text())
        partner.save()
        self.cancel()

    def cancel(self):
        from ui.partners_page import PartnersPage
        self.main_window.setCentralWidget(PartnersPage(self.main_window))
