from taskw import TaskWarrior
from PyQt5.QtWidgets import QWidget, QTabWidget

from .table_widget import PendingTasksTable, CompletedTasksTable


class TaskTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.warrior = TaskWarrior()
        self.tabs = QTabWidget()
        self.pending_table = PendingTasksTable()
        self.completed_table = CompletedTasksTable()

        self.pending_tab = QWidget()
        self.tabs.addTab(self.pending_tab, "Pending")

        self.completed_tab = QWidget()
        self.tabs.addTab(self.completed_tab, "Completed")
