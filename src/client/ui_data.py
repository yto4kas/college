# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_data.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 309)
        Dialog.setStyleSheet(u"background-color: rgb(182, 182, 182)")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"font: 16pt \"Arial\";")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DataContainer = QVBoxLayout()
        self.DataContainer.setObjectName(u"DataContainer")

        self.verticalLayout.addLayout(self.DataContainer)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(Dialog)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(100, 0))
        self.add.setFont(font)

        self.horizontalLayout.addWidget(self.add)

        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(100, 0))
        self.back.setFont(font)

        self.horizontalLayout.addWidget(self.back)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.add.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

