# -*- coding: utf-8 -*-
import os
import sys

from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget, QHBoxLayout, QGroupBox, QPushButton, QVBoxLayout, QTreeWidget, \
    QLabel, QLineEdit, QTextEdit, QTableWidget, QMenuBar, QMenu, QStatusBar, QFormLayout, \
    QAbstractItemView, QComboBox, QToolBar

# base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
base_path = '.'




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 646)
        self.menu_file = QAction(MainWindow)
        self.menu_file.setObjectName(u"menu_file")
        self.login = QAction(MainWindow)
        self.login.setObjectName(u"login")
        icon = QIcon()
        icon.addFile(base_path + "\\static\\image\\login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login.setIcon(icon)
        self.outlogin = QAction(MainWindow)
        self.outlogin.setObjectName(u"outlogin")
        icon1 = QIcon()
        icon1.addFile(base_path + "\\static\\image\\quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.outlogin.setIcon(icon1)
        self.btn_down_email = QAction(MainWindow)
        self.btn_down_email.setObjectName(u"btn_down_email")
        icon2 = QIcon()
        icon2.addFile(base_path + "\\static\\image\\download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_down_email.setIcon(icon2)
        self.btn_export_excel = QAction(MainWindow)
        self.btn_export_excel.setObjectName(u"btn_export_excel")
        icon3 = QIcon()
        icon3.addFile(base_path + "\\static\\image\\excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_excel.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.laeb_employee = QLabel(self.groupBox)
        self.laeb_employee.setObjectName(u"my_label")
        self.laeb_employee.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.laeb_employee)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_employee = QPushButton('新增', self.groupBox)
        self.add_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.add_employee)

        self.del_employee = QPushButton('删除', self.groupBox)
        self.del_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.del_employee)

        self.submit_employee = QPushButton('提交', self.groupBox)
        self.submit_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.submit_employee)

        self.cacell_employee = QPushButton('取消新增', self.groupBox)
        self.cacell_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.cacell_employee)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_employee = QTableWidget(self.groupBox)
        self.table_employee.setObjectName(u"table_employee")

        self.verticalLayout.addWidget(self.table_employee)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_city = QLabel(self.groupBox)
        self.label_city.setObjectName(u"my_label")
        self.label_city.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_city)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_city = QPushButton('新增', self.groupBox)
        self.add_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.add_city)

        self.del_city = QPushButton('删除', self.groupBox)
        self.del_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.del_city)

        self.submit_city = QPushButton('提交', self.groupBox)
        self.submit_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.submit_city)

        self.cancell_city = QPushButton('取消新增', self.groupBox)
        self.cancell_city.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.cancell_city)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.table_city = QTableWidget(self.groupBox)
        self.table_city.setObjectName(u"table_city")

        self.verticalLayout_2.addWidget(self.table_city)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_6.addWidget(self.groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.box_fillter = QGroupBox(self.centralwidget)
        self.box_fillter.setObjectName(u"box_fillter")
        self.horizontalLayout_5 = QHBoxLayout(self.box_fillter)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_year = QLabel(self.box_fillter)
        self.label_year.setObjectName(u"my_label")

        self.horizontalLayout_5.addWidget(self.label_year)

        self.com_year = QComboBox(self.box_fillter)
        self.com_year.setObjectName(u"com_year")

        self.horizontalLayout_5.addWidget(self.com_year)

        self.label_month = QLabel(self.box_fillter)
        self.label_month.setObjectName(u"my_label")

        self.horizontalLayout_5.addWidget(self.label_month)

        self.com_month = QComboBox(self.box_fillter)
        self.com_month.setObjectName(u"com_month")

        self.horizontalLayout_5.addWidget(self.com_month)


        self.verticalLayout_3.addWidget(self.box_fillter)

        self.box_email_detail = QGroupBox(self.centralwidget)
        self.box_email_detail.setObjectName(u"box_email_detail")
        self.horizontalLayout_4 = QHBoxLayout(self.box_email_detail)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeWidget = QTreeWidget(self.box_email_detail)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.treeWidget)

        self.formLayout_email = QFormLayout()
        self.formLayout_email.setObjectName(u"formLayout_email")
        self.line_subject_mail = QLineEdit(self.box_email_detail)
        self.line_subject_mail.setObjectName(u"line_subject_mail")

        self.formLayout_email.setWidget(0, QFormLayout.FieldRole, self.line_subject_mail)

        self.line_send_mail = QLineEdit(self.box_email_detail)
        self.line_send_mail.setObjectName(u"line_send_mail")

        self.formLayout_email.setWidget(1, QFormLayout.FieldRole, self.line_send_mail)

        self.label_subject = QLabel(self.box_email_detail)
        self.label_subject.setObjectName(u"my_label")

        self.formLayout_email.setWidget(0, QFormLayout.LabelRole, self.label_subject)

        self.label_send_mail = QLabel(self.box_email_detail)
        self.label_send_mail.setObjectName(u"my_label")

        self.formLayout_email.setWidget(1, QFormLayout.LabelRole, self.label_send_mail)

        self.label_content_email = QLabel(self.box_email_detail)
        self.label_content_email.setObjectName(u"my_label")

        self.formLayout_email.setWidget(2, QFormLayout.LabelRole, self.label_content_email)

        self.text_content_mail = QTextEdit(self.box_email_detail)
        self.text_content_mail.setObjectName(u"text_content_mail")

        self.formLayout_email.setWidget(2, QFormLayout.FieldRole, self.text_content_mail)


        self.horizontalLayout_4.addLayout(self.formLayout_email)


        self.verticalLayout_3.addWidget(self.box_email_detail)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar_obj = QMenuBar(MainWindow)
        self.menubar_obj.setObjectName(u"menubar_obj")
        self.menubar_obj.setGeometry(QRect(0, 0, 1090, 26))
        self.menu_file_2 = QMenu(self.menubar_obj)
        self.menu_file_2.setObjectName(u"menu_file_2")
        self.menuyoujian = QMenu(self.menubar_obj)
        self.menuyoujian.setObjectName(u"menuyoujian")
        MainWindow.setMenuBar(self.menubar_obj)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar_obj.addAction(self.menu_file_2.menuAction())
        self.menubar_obj.addAction(self.menuyoujian.menuAction())
        self.menu_file_2.addAction(self.login)
        self.menu_file_2.addAction(self.outlogin)
        self.menuyoujian.addAction(self.btn_down_email)
        self.menuyoujian.addAction(self.btn_export_excel)
        self.toolBar.addAction(self.login)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_down_email)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_export_excel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.outlogin)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_file.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1\u767b\u5f55", None))
        self.login.setToolTip(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1\u767b\u5f55", None))
        self.outlogin.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.outlogin.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.outlogin.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
        self.btn_down_email.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u4e0b\u8f7d", None))
        self.btn_down_email.setToolTip(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u4e0b\u8f7d", None))
        self.btn_export_excel.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8868\u683c", None))
        self.btn_export_excel.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8868\u683c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7ba1\u7406", None))
        self.laeb_employee.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u6210\u5458\u85aa\u8d44\u5bf9\u7167\u8868", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u5dee\u57ce\u5e02\u8865\u8d34\u5bf9\u7167", None))
        self.box_fillter.setTitle(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u4e0b\u8f7d\u8fc7\u6ee4", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u4efd\uff1a", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"\u6708\u4efd\uff1a", None))
        self.box_email_detail.setTitle(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u8be6\u60c5", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"邮件树", None))
        self.label_subject.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u4e3b\u9898 ", None))
        self.label_send_mail.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u4ef6\u4eba", None))
        self.label_content_email.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u5185\u5bb9", None))
        self.menu_file_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuyoujian.setTitle(QCoreApplication.translate("MainWindow", u"\u90ae\u4ef6\u64cd\u4f5c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

        # style
        self.table_city.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_city.setMaximumWidth(300)
        self.table_employee.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_employee.setMinimumWidth(530)
        self.treeWidget.horizontalScrollBar()
        self.treeWidget.header().setMinimumSectionSize(700)
        self.treeWidget.setMinimumWidth(250)
        for item in self.groupBox.findChildren(QPushButton, 'btn_all'):
            item.setMaximumWidth(70)
        for item in self.groupBox.findChildren(QPushButton, 'btn_all_emp'):
            item.setMaximumWidth(100)
        for item in self.groupBox.findChildren(QPushButton, 'btn_cancel'):
            item.setMaximumWidth(90)
        # 取父控件下的所有子类： 需要注意的是childern() 利用 inherits() 过滤出需要的子类
        for item in self.box_email_detail.children():
            if item.inherits('QLineEdit') or item.inherits('QTextEdit'):
                item.setFocusPolicy(Qt.NoFocus)

        # QMenuBar：菜单栏  QMenu： 菜单下拉栏  QToolBar：工具栏