import sys
import breeze_resources
from PyQt5.QtCore import QFile, QTextStream

from PyQt5.QtWidgets import QApplication
from sethrak.gui.main_window import MainWindow


def run():

    app = QApplication(sys.argv)

    file = QFile(":/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    window = MainWindow()
    window.show()

    app.exec_()
