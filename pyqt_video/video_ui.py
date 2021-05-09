# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from utils import set_font
from video_win import myVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.left_box = QVBoxLayout()
        self.label_dir = QLabel()
        self.label_dir.setText('文件目录区')
        self.label_dir.setMinimumSize(50, 120)
        font = set_font(weight=70)
        self.label_dir.setFont(font)
        self.label_dir.setStyleSheet("color: rgb(255, 255, 255);\nbackground-color: rgb(88, 94, 92);")

        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(300, 500)
        self.treeWidget.setMaximumSize(QtCore.QSize(400, 2000))
        self.treeWidget.header().setMinimumSectionSize(1500)
        self.treeWidget.setStyleSheet("color: rgb(255, 255, 255);"
                                      "font-size: 12pt;"
                                      "\nbackground-color: rgb(88, 94, 92);"
                                      "\ntext-align:center;")
        font = set_font()
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.left_box.addWidget(self.label_dir)
        self.left_box.addWidget(self.treeWidget)
        self.horizontalLayout_5.addLayout(self.left_box)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalFrame1 = QtWidgets.QFrame(self.frame)
        self.verticalFrame1.setMaximumSize(QtCore.QSize(1666666, 162))
        self.verticalFrame1.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                          "color: rgb(255, 255, 255);")
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalFrame1)
        self.label_6.setObjectName("label_6")
        font = set_font(weight=70)
        self.label_6.setFont(font)
        self.horizontalLayout_6.addWidget(self.label_6)
        self.btn_6 = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_6.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_6.addWidget(self.btn_6)
        self.btn_7 = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_7.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout_6.addWidget(self.btn_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.video_name = QtWidgets.QLabel(self.verticalFrame1)
        self.video_name.setObjectName("video_name")
        self.horizontalLayout_7.addWidget(self.video_name)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_choose = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_choose.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_choose.setObjectName("btn_choose")
        self.horizontalLayout_8.addWidget(self.btn_choose)
        self.btn_choose_videos = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_choose_videos.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                             "color: rgb(255, 255, 255);")
        self.btn_choose_videos.setObjectName("btn_choose_videos")
        self.horizontalLayout_8.addWidget(self.btn_choose_videos)
        self.btn_1 = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_1.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_8.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_2.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_8.addWidget(self.btn_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.verticalFrame1)
        self.widget = myVideoWidget(self.frame)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(15000, 700)
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sld_video = QtWidgets.QSlider(self.frame_2)
        self.sld_video.setStyleSheet("QSlider::groove:horizontal {\n"
                                     "border: 1px solid #4A708B;\n"
                                     "background: #C0C0C0;\n"
                                     "height: 5px;\n"
                                     "border-radius: 1px;\n"
                                     "padding-left:-1px;\n"
                                     "padding-right:-1px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal {\n"
                                     "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
                                     "    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                     "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                     "    stop: 0 #5DCCFF, stop: 1 #1874CD);\n"
                                     "border: 1px solid #4A708B;\n"
                                     "height: 10px;\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal {\n"
                                     "background: #575757;\n"
                                     "border: 0px solid #777;\n"
                                     "height: 10px;\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal \n"
                                     "{\n"
                                     "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
                                     "    stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));\n"
                                     "\n"
                                     "    width: 11px;\n"
                                     "    margin-top: -3px;\n"
                                     "    margin-bottom: -3px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:hover {\n"
                                     "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, \n"
                                     "    stop:0.778409 rgba(255, 255, 255, 255));\n"
                                     "\n"
                                     "    width: 11px;\n"
                                     "    margin-top: -3px;\n"
                                     "    margin-bottom: -3px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal:disabled {\n"
                                     "background: #00009C;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border: 1px solid #aaa;\n"
                                     "border-radius: 4px;\n"
                                     "}")
        self.sld_video.setPageStep(5)
        self.sld_video.setTracking(True)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.horizontalLayout_10.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.frame_2)
        self.lab_video.setObjectName("lab_video")
        self.horizontalLayout_10.addWidget(self.lab_video)
        self.lab_video_start = QtWidgets.QLabel(self.frame_2)
        self.lab_video_start.setObjectName("lab_video_start")
        self.horizontalLayout_10.addWidget(self.lab_video_start)
        self.voice_video = QtWidgets.QLabel(self.frame_2)
        self.voice_video.setObjectName("voice_video")
        self.horizontalLayout_10.addWidget(self.voice_video)
        self.horizontalLayout_9.addWidget(self.frame_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.quick_back = QtWidgets.QPushButton(self.frame_4)
        self.quick_back.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                      "color: rgb(255, 255, 255);")
        self.quick_back.setObjectName("quick_forward")
        self.horizontalLayout_12.addWidget(self.quick_back)
        self.btn_4 = QtWidgets.QPushButton(self.frame_4)
        self.btn_4.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_12.addWidget(self.btn_4)
        self.btn_play = QtWidgets.QPushButton(self.frame_4)
        self.btn_play.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_12.addWidget(self.btn_play)
        self.btn_stop = QtWidgets.QPushButton(self.frame_4)
        self.btn_stop.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_12.addWidget(self.btn_stop)
        self.quick_forward = QtWidgets.QPushButton(self.frame_4)
        self.quick_forward.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.quick_forward.setObjectName("quick_forward")
        self.horizontalLayout_12.addWidget(self.quick_forward)
        self.horizontalLayout_13.addWidget(self.frame_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addWidget(self.frame)
        self.horizontalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame1.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalFrame1.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.verticalLayout_8.addWidget(self.horizontalFrame1)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "宋章梦"))
        self.label_6.setText(_translate("MainWindow", "视频播放区"))
        self.btn_6.setText(_translate("MainWindow", "待定6"))
        self.btn_7.setText(_translate("MainWindow", "待定7"))
        self.video_name.setText(_translate("MainWindow", "当前播放："))
        self.btn_choose.setText(_translate("MainWindow", "选择单个文件"))
        self.btn_choose_videos.setText(_translate("MainWindow", "批量导入文件"))
        self.btn_1.setText(_translate("MainWindow", "待定1"))
        self.btn_2.setText(_translate("MainWindow", "待定2"))
        self.lab_video.setText(_translate("MainWindow", "|00:00"))
        self.lab_video_start.setText(_translate("MainWindow", "|00:00"))
        self.voice_video.setText(_translate("MainWindow", "|50%|"))
        self.quick_back.setText(_translate("MainWindow", "快退 <<< 5秒"))
        self.btn_4.setText(_translate("MainWindow", "待定4"))
        self.btn_play.setText(_translate("MainWindow", "开始/暂停"))
        self.btn_stop.setText(_translate("MainWindow", "停止"))
        self.quick_forward.setText(_translate("MainWindow", "快进 >>> 5秒"))
        
        
        self.quick_back.setToolTip('左键快退')
        self.quick_forward.setToolTip('右键快退')
        self.btn_play.setStyleSheet('color: yellow')
        self.quick_back.setStyleSheet('color: red')
        self.quick_forward.setStyleSheet('color: red')
        self.voice_video.setStyleSheet('color: red')
        self.lab_video.setStyleSheet('color: yellow')
        self.lab_video_start.setStyleSheet('color: yellow')
        self.voice_video.setToolTip('up 增加 down 降低')

        font = set_font(weight=50)
        font_list = [self.btn_6, self.btn_7, self.video_name, self.btn_choose, self.btn_choose_videos, self.btn_1,
                     self.btn_2, self.lab_video, self.lab_video_start, self.voice_video, self.quick_forward, self.quick_back, self.btn_4, self.btn_play,
                     self.btn_stop]
        [item.setFont(font) for item in font_list]

        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"根目录", None))
        ___qtreewidgetitem.setForeground(0, Qt.black)
