# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, Qt, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget, QHBoxLayout, QSplitter, QTreeWidget, QTreeWidgetItem, QLabel, QTextEdit, \
    QMenuBar, QMenu, QStatusBar, QToolBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 861)
        self.insert_img = QAction(MainWindow)
        self.insert_img.setObjectName(u"insert_img")
        self.insert_img.setCheckable(True)
        icon = QIcon()
        icon.addFile(u"D:/background/b_background/dog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insert_img.setIcon(icon)
        self.more_insert_img = QAction(MainWindow)
        self.more_insert_img.setObjectName(u"more_insert_img")
        icon1 = QIcon()
        icon1.addFile(u"D:/background/b_background/cc2e9d9b67b48bd74e1afba11912d0d7.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.more_insert_img.setIcon(icon1)
        self.quit_windown = QAction(MainWindow)
        self.quit_windown.setObjectName(u"quit_windown")
        icon2 = QIcon()
        icon2.addFile(u"D:/background/b_background/kpg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_windown.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeWidget = QTreeWidget(self.splitter)
        self.treeWidget.setObjectName(u"treeWidget")
        self.splitter.addWidget(self.treeWidget)
        self.img_label = QLabel(self.splitter)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setMinimumSize(QSize(700, 100))
        self.splitter.addWidget(self.img_label)
        self.img_info = QTextEdit(self.splitter)
        self.img_info.setObjectName(u"img_info")
        self.splitter.addWidget(self.img_info)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1094, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.insert_img)
        self.menu.addAction(self.more_insert_img)
        self.menu.addAction(self.quit_windown)
        self.toolBar.addAction(self.insert_img)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.more_insert_img)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.quit_windown)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.insert_img.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u7247", None))
#if QT_CONFIG(tooltip)
        self.insert_img.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.more_insert_img.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165\u56fe\u7247", None))
#if QT_CONFIG(tooltip)
        self.more_insert_img.setToolTip(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.quit_windown.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.quit_windown.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6839\u76ee\u5f55", None));
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)

        self.img_label.setText(QCoreApplication.translate("MainWindow", u"v\u72af\u5f97\u4e0a\u53d1\u751f\u53d8\u66f4\u53d1\u8868\u89c2\u70b9 ", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

