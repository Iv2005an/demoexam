from PySide6.QtWidgets import QWidget

from database.models import Partner
from ui.partner_card import PartnerCard
from ui.ui_partners_page import Ui_partnersPage


class PartnersPage(QWidget, Ui_partnersPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageTitle.setText("Список партнёров")
        partners = Partner.get_all()
        partners_area = self.partnersAreaLayout.layout()
        for partner in partners:
            partners_area.addWidget(PartnerCard(partner))
