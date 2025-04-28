# -*- coding: utf-8 -*-
import os
import sys

from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget, QHBoxLayout, QGroupBox, QPushButton, QVBoxLayout, QTreeWidget, \
    QLabel, QLineEdit, QTextEdit, QTableWidget, QMenuBar, QMenu, QStatusBar, QFormLayout, \
    QAbstractItemView, QComboBox, QToolBar
from qfluentwidgets import (FluentWindow, PushButton, LineEdit,
                           setTheme, Theme, setThemeColor,
                           NavigationItemPosition, FluentIcon, TableWidget, TreeWidget)
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
        self.add_employee = PushButton('新增', self.groupBox)
        self.add_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.add_employee)

        self.del_employee = PushButton('删除', self.groupBox)
        self.del_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.del_employee)

        self.submit_employee = PushButton('提交', self.groupBox)
        self.submit_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.submit_employee)

        self.cacell_employee = PushButton('取消新增', self.groupBox)
        self.cacell_employee.setObjectName(u"btn_all_emp")

        self.horizontalLayout.addWidget(self.cacell_employee)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_employee = TableWidget(self.groupBox)
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
        self.add_city = PushButton('新增', self.groupBox)
        self.add_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.add_city)

        self.del_city = PushButton('删除', self.groupBox)
        self.del_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.del_city)

        self.submit_city = PushButton('提交', self.groupBox)
        self.submit_city.setObjectName(u"btn_all")

        self.horizontalLayout_2.addWidget(self.submit_city)

        self.cancell_city = PushButton('取消新增', self.groupBox)
        self.cancell_city.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.cancell_city)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.table_city = TableWidget(self.groupBox)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.menu_file.setText(QCoreApplication.translate("MainWindow", "文件", None))
        self.menu_file.setToolTip(QCoreApplication.translate("MainWindow", "文件", None))
        self.login.setText(QCoreApplication.translate("MainWindow", "邮箱登录", None))
        self.login.setToolTip(QCoreApplication.translate("MainWindow", "邮箱登录", None))
        self.outlogin.setText(QCoreApplication.translate("MainWindow", "退出", None))
        self.outlogin.setToolTip(QCoreApplication.translate("MainWindow", "退出", None))
        self.outlogin.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Q", None))
        self.btn_down_email.setText(QCoreApplication.translate("MainWindow", "邮件下载", None))
        self.btn_down_email.setToolTip(QCoreApplication.translate("MainWindow", "邮件下载", None))
        self.btn_export_excel.setText(QCoreApplication.translate("MainWindow", "导出表格", None))
        self.btn_export_excel.setToolTip(QCoreApplication.translate("MainWindow", "导出表格", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "项目管理", None))

        self.laeb_employee.setText(QCoreApplication.translate("MainWindow", "项目成员薪资对照表", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", "出差城市补贴对照", None))
        self.box_fillter.setTitle(QCoreApplication.translate("MainWindow", "邮件下载过滤", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", "年份：", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", "月份：", None))
        self.box_email_detail.setTitle(QCoreApplication.translate("MainWindow", "邮件详情", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", "邮件树", None))
        self.label_subject.setText(QCoreApplication.translate("MainWindow", "邮件主题 ", None))
        self.label_send_mail.setText(QCoreApplication.translate("MainWindow", "发件人", None))
        self.label_content_email.setText(QCoreApplication.translate("MainWindow", "邮件内容", None))
        self.menu_file_2.setTitle(QCoreApplication.translate("MainWindow", "文件", None))
        self.menuyoujian.setTitle(QCoreApplication.translate("MainWindow", "邮件操作", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", "toolBar", None))

        # style
        self.table_city.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_city.setMaximumWidth(300)
        self.table_employee.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_employee.setMinimumWidth(530)
        self.treeWidget.horizontalScrollBar()
        self.treeWidget.header().setMinimumSectionSize(700)
        self.treeWidget.setMinimumWidth(250)
        for item in self.groupBox.findChildren(PushButton, 'btn_all'):
            item.setMaximumWidth(70)
        for item in self.groupBox.findChildren(PushButton, 'btn_all_emp'):
            item.setMaximumWidth(100)
        for item in self.groupBox.findChildren(PushButton, 'btn_cancel'):
            item.setMaximumWidth(90)
        # 取父控件下的所有子类： 需要注意的是childern() 利用 inherits() 过滤出需要的子类
        for item in self.box_email_detail.children():
            if item.inherits('QLineEdit') or item.inherits('QTextEdit'):
                item.setFocusPolicy(Qt.NoFocus)

        # QMenuBar：菜单栏  QMenu： 菜单下拉栏  QToolBar：工具栏