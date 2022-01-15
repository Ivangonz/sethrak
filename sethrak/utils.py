from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication


def toggle_stylesheet(path):

    app = QApplication.instance()
    if app is None:
        raise RuntimeError("No Qt Application found.")

    file = QFile(path)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
