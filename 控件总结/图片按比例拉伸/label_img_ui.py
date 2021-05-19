# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QLabel, QTableWidget, QMenuBar, QStatusBar

from 控件总结.图片按比例拉伸.img_ui import MyLabel
from 控件总结.图片按比例拉伸.table_ui import MyTable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(660, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = MyLabel(self.splitter)
        self.splitter.addWidget(self.label)
        self.table_view = MyTable(self.splitter)

        self.splitter.addWidget(self.table_view)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

