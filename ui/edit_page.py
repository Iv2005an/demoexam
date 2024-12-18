from PySide6.QtWidgets import QWidget, QMainWindow

from database.models import Partner
from ui.ui_edit_page import Ui_editPage


class EditPage(QWidget, Ui_editPage):
    def __init__(self, main_window: QMainWindow, partner: Partner):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.partner = partner
        self.nameTitle.setText("Наименование:")
        self.nameField.setText(self.partner.name)
        self.typeTitle.setText("Тип:")
        self.typeField.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        self.typeField.setCurrentText(self.partner.type)
        self.innTitle.setText("ИНН:")
        self.innField.setText(self.partner.inn)
        self.rateTitle.setText("Рейтинг:")
        self.rateField.setValue(self.partner.rate)
        self.addressTitle.setText("Адрес:")
        self.addressField.setText(self.partner.address)
        self.directorTitle.setText("Директор:")
        self.directorFiled.setText(self.partner.director)
        self.phoneTitle.setText("Телефон:")
        self.phoneField.setText(self.partner.phone)
        self.emailTitle.setText("Почта:")
        self.emailField.setText(self.partner.email)
        self.editButton.setText("Редактировать")
        self.editButton.clicked.connect(self.edit)
        self.cancelButton.setText("Отмена")
        self.cancelButton.clicked.connect(self.cancel)

    def edit(self):
        self.partner.name = self.nameField.text()
        self.partner.type = self.typeField.currentText()
        self.partner.inn = self.innField.text()
        self.partner.rate = self.rateField.text()
        self.partner.address = self.addressField.text()
        self.partner.director = self.directorFiled.text()
        self.partner.phone = self.phoneField.text()
        self.partner.email = self.emailField.text()
        self.partner.save()
        self.cancel()

    def cancel(self):
        from ui.partners_page import PartnersPage
        self.main_window.setCentralWidget(PartnersPage(self.main_window))
