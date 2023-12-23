from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtCore import Qt
from src.client.ui_main import Ui_MainWindow
from src.client.DataWindow import DataWindow
from src.client.api.resolver import *
from src.client.api.statistics import update_statistics

TablesList = ["Users", "subject", "Teachers", "Students","Courses","Enrollment","Grades",]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.current_table_index = None
        self.current_table_keys = []
        self.user_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ShowTables.clicked.connect(lambda: self.ChangeTab(0))
        self.ui.ShowStats.clicked.connect(lambda: self.ChangeTab(1))
        self.ui.Add.clicked.connect(self.OpenNewWindow)
        self.ui.Update.clicked.connect(self.OpenNewWindow)
        self.ui.Delete.clicked.connect(self.delete_data)
        self.ui.LoginButton.clicked.connect(self.Login)
        self.ui.TableSearch.textChanged.connect(self.Search)

        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.navButtons.setVisible(False)

        table_list = self.ui.TabelList
        table_list.currentRowChanged.connect(self.TableSelect)
        table_list.addItems(TablesList)

    def Login(self):
        self.user_data = login(self.ui.loginText.text(), self.ui.passwordText.text())
        print(self.user_data)
        if not self.user_data:
            self.ui.loginInfo.setText("Неверный логин или пароль")
            return

        self.ui.navButtons.setVisible(True)
        self.ui.stackedWidget.setCurrentIndex(0)

        if self.user_data[3] == 1:
            self.ui.TabelList.setEnabled(False)
            self.TableSelect(1)
            self.ui.Add.setEnabled(False)
            self.ui.Delete.setEnabled(False)
        print("Доступ :", self.user_data[3])

    def TableSelect(self, table_index):
        print(f"Таблица: {table_index}")
        self.current_table_index = table_index
        self.UpdateTableData()

    def UpdateTableData(self):
        data = getAll(TablesList[self.current_table_index])
        if not data: return
        self.current_table_keys = data[0].keys()

        if self.user_data[3] == 1:
            data = self.sort_data_on_id(data)
            if not data: return

        table = self.ui.Table
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(list(data[0].keys()))
        table.setColumnWidth(0, 60)

        row_index = 0
        for values in data:
            for item in values.values():
                for i in range(len(data[0])):
                    table.setItem(i, row_index, QTableWidgetItem(str(item)))
                row_index += 1

    def sort_data_on_id(self, data):
        new_data = []
        for item in data:
            if "user_id" not in item: return
            if item["user_id"] == self.user_data[0]:
                new_data.append(item)
        return new_data

    def ChangeTab(self, tab_index):
        self.ui.ShowTables.setEnabled(not self.ui.ShowTables.isEnabled())
        self.ui.ShowStats.setEnabled(not self.ui.ShowStats.isEnabled())

        if not self.ui.ShowStats.isEnabled():
            update_statistics(self.ui.CompleteSum, self.ui.AvgCompletionTime, self.ui.DiseaseTypes)

        self.ui.stackedWidget.setCurrentIndex(tab_index)

    def Search(self, search):
        table = self.ui.Table
        table.setCurrentItem(None)
        if not search: return
        matching_items = table.findItems(search, Qt.MatchFlag.MatchContains)
        if not matching_items: return
        table.setCurrentItem(matching_items[0])

    def OpenNewWindow(self):
        self.data_window = DataWindow(self.user_data[3], TablesList[self.current_table_index])

        sender = self.sender()
        if sender.objectName() == "Add":
            self.data_window.ui.add.clicked.connect(self.add_data)
            self.data_window.ui.label.setText("Создать запись")
            self.data_window.ui.add.setText("Создать")
        else:
            self.data_window.SetData(self.ui.Table)
            self.data_window.ui.add.clicked.connect(self.update_data)
            self.data_window.ui.label.setText("Обновить запись")
            self.data_window.ui.add.setText("Обновить")

    def get_model(self) -> dict:
        values: list = self.data_window.GetData()
        self.data_window.close()
        return dict(zip(self.current_table_keys, values))

    def get_current_id(self) -> int:
        index = self.ui.Table.selectedIndexes()[0]
        return self.ui.Table.model().data(index)

    def add_data(self):
        create(TablesList[self.current_table_index], self.get_model())
        self.UpdateTableData()

    def update_data(self):
        update(TablesList[self.current_table_index], self.get_model(), self.get_current_id())
        self.UpdateTableData()

    def delete_data(self):
        ret = QMessageBox.warning(self, "Подтверждение", f"Вы хотите удалить запись с id:{self.get_current_id()}",
                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if ret != QMessageBox.StandardButton.Yes:
            return

        delete(TablesList[self.current_table_index], self.get_current_id())
        self.UpdateTableData()
