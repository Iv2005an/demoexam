from PySide6.QtWidgets import QWidget

from ui.ui_partners_page import Ui_partnersPage


class PartnersPage(QWidget, Ui_partnersPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageTitle.setText("Страница партнёров")
