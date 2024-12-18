from PySide6.QtWidgets import QWidget, QMainWindow

from database.models import Partner
from ui.add_page import AddPage
from ui.partner_card import PartnerCard
from ui.ui_partners_page import Ui_partnersPage


class PartnersPage(QWidget, Ui_partnersPage):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pageTitle.setText("Список партнёров")
        self.addButton.setText("Добавить партнёра")
        self.addButton.clicked.connect(self.add_partner)
        partners = Partner.get_all()
        partners_area = self.partnersAreaLayout.layout()
        for partner in partners:
            partners_area.addWidget(PartnerCard(self.main_window, partner))

    def add_partner(self):
        self.main_window.setCentralWidget(AddPage(self.main_window))
