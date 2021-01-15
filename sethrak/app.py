import sys
from sethrak.gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def run():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
