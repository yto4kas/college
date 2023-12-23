# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 675)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navButtons = QWidget(self.centralwidget)
        self.navButtons.setObjectName(u"navButtons")
        self.navButtons.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.navButtons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layouy = QHBoxLayout()
        self.layouy.setObjectName(u"layouy")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.layouy.addItem(self.horizontalSpacer_3)

        self.ShowTables = QPushButton(self.navButtons)
        self.ShowTables.setObjectName(u"ShowTables")
        self.ShowTables.setEnabled(False)
        self.ShowTables.setMinimumSize(QSize(250, 0))
        self.ShowTables.setFont(font)

        self.layouy.addWidget(self.ShowTables)

        self.ShowStats = QPushButton(self.navButtons)
        self.ShowStats.setObjectName(u"ShowStats")
        self.ShowStats.setEnabled(True)
        self.ShowStats.setMinimumSize(QSize(250, 0))
        self.ShowStats.setFont(font)

        self.layouy.addWidget(self.ShowStats)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layouy.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.layouy)


        self.verticalLayout_2.addWidget(self.navButtons)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        font1 = QFont()
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.stackedWidget.setFont(font1)
        self.Tables = QWidget()
        self.Tables.setObjectName(u"Tables")
        self.horizontalLayout_3 = QHBoxLayout(self.Tables)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.TabelList = QListWidget(self.Tables)
        self.TabelList.setObjectName(u"TabelList")
        self.TabelList.setMinimumSize(QSize(200, 0))
        self.TabelList.setMaximumSize(QSize(250, 16777215))
        self.TabelList.setFont(font)

        self.horizontalLayout_3.addWidget(self.TabelList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Add = QPushButton(self.Tables)
        self.Add.setObjectName(u"Add")
        self.Add.setMinimumSize(QSize(200, 0))
        self.Add.setFont(font)

        self.horizontalLayout.addWidget(self.Add)

        self.Update = QPushButton(self.Tables)
        self.Update.setObjectName(u"Update")
        self.Update.setMinimumSize(QSize(200, 0))
        self.Update.setFont(font)

        self.horizontalLayout.addWidget(self.Update)

        self.Delete = QPushButton(self.Tables)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setMinimumSize(QSize(200, 0))
        self.Delete.setFont(font)

        self.horizontalLayout.addWidget(self.Delete)

        self.TableSearch = QLineEdit(self.Tables)
        self.TableSearch.setObjectName(u"TableSearch")
        self.TableSearch.setFont(font)

        self.horizontalLayout.addWidget(self.TableSearch)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Table = QTableWidget(self.Tables)
        self.Table.setObjectName(u"Table")
        self.Table.setFont(font)
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Table.setTextElideMode(Qt.ElideNone)
        self.Table.horizontalHeader().setVisible(True)
        self.Table.horizontalHeader().setMinimumSectionSize(60)
        self.Table.horizontalHeader().setDefaultSectionSize(200)
        self.Table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.Table)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.Tables)
        self.Stats = QWidget()
        self.Stats.setObjectName(u"Stats")
        self.Stats.setStyleSheet(u"font: 16pt \"Arial\";")
        self.horizontalLayout_4 = QHBoxLayout(self.Stats)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.AvgCompletionTime = QLabel(self.Stats)
        self.AvgCompletionTime.setObjectName(u"AvgCompletionTime")

        self.verticalLayout_5.addWidget(self.AvgCompletionTime)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.CompleteSum = QLabel(self.Stats)
        self.CompleteSum.setObjectName(u"CompleteSum")

        self.verticalLayout_5.addWidget(self.CompleteSum)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.widget = QWidget(self.Stats)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AvgCompletionTime_2 = QLabel(self.widget)
        self.AvgCompletionTime_2.setObjectName(u"AvgCompletionTime_2")

        self.verticalLayout_7.addWidget(self.AvgCompletionTime_2)

        self.DiseaseTypes = QListWidget(self.widget)
        self.DiseaseTypes.setObjectName(u"DiseaseTypes")

        self.verticalLayout_7.addWidget(self.DiseaseTypes)


        self.horizontalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.Stats)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayoutWidget_2 = QWidget(self.login)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(380, 170, 321, 231))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(24)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.loginText = QLineEdit(self.verticalLayoutWidget_2)
        self.loginText.setObjectName(u"loginText")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        self.loginText.setFont(font3)

        self.verticalLayout_3.addWidget(self.loginText)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.passwordText = QLineEdit(self.verticalLayoutWidget_2)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setFont(font3)

        self.verticalLayout_3.addWidget(self.passwordText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.LoginButton = QPushButton(self.verticalLayoutWidget_2)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.LoginButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.loginInfo = QLabel(self.verticalLayoutWidget_2)
        self.loginInfo.setObjectName(u"loginInfo")
        self.loginInfo.setFont(font)
        self.loginInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.loginInfo)

        self.stackedWidget.addWidget(self.login)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShowTables.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.ShowStats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.TableSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e ID", None))
        self.AvgCompletionTime.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.CompleteSum.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.AvgCompletionTime_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0439", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.loginText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwordText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.loginInfo.setText("")
    # retranslateUi

