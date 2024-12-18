from PySide6.QtWidgets import QWidget, QMainWindow

from database.models import Partner
from ui.edit_page import EditPage
from ui.ui_partner_card import Ui_partnerCard


class PartnerCard(QWidget, Ui_partnerCard):
    def __init__(self, main_window: QMainWindow, partner: Partner):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.partner = partner
        self.title.setText(f"{partner.type} | {partner.name}")
        self.director.setText(f"Директор: {partner.director}")
        self.phone.setText(f"Телефон: +7 {partner.phone}")
        self.rate.setText(f"Рейтинг: {partner.rate}")
        self.discount.setText(f"{partner.discount}%")

    def mousePressEvent(self, event):
        self.main_window.setCentralWidget(EditPage(self.main_window, self.partner))
