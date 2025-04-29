from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QMenuBar, QStatusBar
from img_ui import MyLabel
from table_ui import MyTable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)

        self.splitter = QSplitter(Qt.Horizontal)
        self.label = MyLabel(self.splitter)
        self.table_view = MyTable(self.splitter)

        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Fluent Window Demo", None))
