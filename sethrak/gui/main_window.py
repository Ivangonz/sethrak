from .task_tabs import *


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Sethrak - TaskWarrior")
        self.setMinimumHeight(300)
        self.central_widget = PendingTasksTable()
        self.setCentralWidget(self.central_widget)
