from PyQt5.QtWidgets import QMainWindow

from .table_widget import PendingTasksTable


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Sethrak - TaskWarrior")
        self.setMinimumHeight(300)
        self.central_widget = PendingTasksTable()
        self.setCentralWidget(self.central_widget)
