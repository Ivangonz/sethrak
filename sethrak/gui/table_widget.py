from taskw import TaskWarrior
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidget, QAbstractScrollArea, QTableView, QTableWidgetItem


class TableWidget(QTableWidget):

    def __init__(self):
        super().__init__()
        self.warrior = TaskWarrior()

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)

    def show_items(self, task_list):
        self.setRowCount(len(task_list))

        for row, item_list in enumerate(task_list):
            for col, key in enumerate(item_list):
                new_item = QTableWidgetItem(item_list[key])
                self.setItem(row, col, new_item)

        self.resizeColumnsToContents()


class PendingTasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(5)
        self.setHorizontalHeaderLabels([
            "TaskID",
            "Description",
            "Entered",
            "Modified",
            "Status",
        ])

        self.show_items(self.get_pending())

    def get_pending(self):
        return self.warrior.load_tasks().get('pending')


class CompletedTasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["TaskID", "Description", "Completed", "Entered"])

    def get_completed(self):
        return self.warrior.load_tasks('completed').get('completed')
