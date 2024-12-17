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