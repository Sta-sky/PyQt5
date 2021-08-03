# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize, QMetaObject
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, \
    QPushButton, QDialog



class LoginUI(QDialog):
    def setupUi(self, QDialog):
        if QDialog.objectName():
            QDialog.setObjectName(u"QDialog")
        QDialog.resize(830, 479)
        self.horizontalLayout = QHBoxLayout(QDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.box_email_login = QGroupBox('邮箱登录', QDialog)
        self.box_email_login.setObjectName(u"box_email_login")
        self.verticalLayout_2 = QVBoxLayout(self.box_email_login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_account = QLabel('邮箱账号', self.box_email_login)
        self.label_account.setObjectName(u"label_account")
        self.label_account.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_account)

        self.line_account = QLineEdit(self.box_email_login)
        self.line_account.setObjectName(u"line_account")
        self.line_account.setMinimumSize(QSize(450, 0))

        self.horizontalLayout_2.addWidget(self.line_account)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_password = QLabel('邮箱密码', self.box_email_login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_password)

        self.line_password = QLineEdit(self.box_email_login)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setMinimumSize(QSize(450, 0))

        self.horizontalLayout_3.addWidget(self.line_password)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_login = QPushButton('登录', self.box_email_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.btn_login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.box_email_login)

        self.line_password.setEchoMode(QLineEdit.Password)
        QMetaObject.connectSlotsByName(QDialog)
    # setupUi



