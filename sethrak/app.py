import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import (
    QMenu,
    QAction,
    QApplication,
    QSystemTrayIcon,
)
from sethrak.gui.main_window import MainWindow


def run():

    app = QApplication(sys.argv)

    app.setQuitOnLastWindowClosed(False)

    # Adding an icon
    icon = QIcon("snek.png")

    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QMenu()
    option1 = QAction("New Task")
    menu.addAction(option1)

    # To quit the app
    quit_app = QAction("Quit")
    quit_app.triggered.connect(app.quit)
    menu.addAction(quit_app)

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    file = QFile(":/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    window = MainWindow()
    window.show()

    app.exec_()
