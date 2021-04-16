from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout


class SetLabel:
    def label_init(self, Baseform):
        self.label_view = QLabel(Baseform)
        self.label_view.setText("这是一个图片显示框")
        self.label_view.setPixmap(QPixmap('./test.jpg'))
        self.label_view.setScaledContents(True)
        self.label_view.setGeometry(QtCore.QRect(50, 150, 700, 550))

        # 初始化一个label框
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.img_label = QLabel(Baseform)
        self.img_label.setFont(font)
        # 设置label的位置
        self.img_label.setGeometry(QtCore.QRect(200, 700, 400, 50))
        # self.img_label.setStyleSheet('background-color: red;')

        self.img_btn1 = QPushButton("Table View 格式显示")
        self.img_btn2 = QPushButton("wafer View 格式显示")
        # 初始化一个 垂直 布局管理器
        self.v_lable = QHBoxLayout()
        self.v_lable.addWidget(self.img_btn1)
        self.v_lable.addWidget(self.img_btn2)
        # 将布局管理器加入标签控件中
        self.img_label.setLayout(self.v_lable)

        self.img_btn1.clicked.connect(self.img_btn1_Clicked)
        self.img_btn2.clicked.connect(self.img_btn2_Clicked)

    def img_btn1_Clicked(self):
        self.label_view.setPixmap(QPixmap('./test.jpg'))

    def img_btn2_Clicked(self, info):
        self.label_view.setPixmap(QPixmap('./test1.png'))
