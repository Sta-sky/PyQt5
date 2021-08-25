# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect
from PyQt5.QtGui import QIcon, QBrush, QColor, QFont
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QSlider, QAction, QSplitter, QGroupBox, \
    QToolTip

from utils import set_font
from video_win import myVideoWidget

# static_base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
static_base_path = '.'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.outlogin = QAction(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.left_box = QVBoxLayout()
        font = set_font(weight=70)
        self.video_list_region = QLabel('视频播放列表')
        self.video_list_region.setObjectName('label')
        self.video_list_region.setFont(font)
        self.treeWidget = QtWidgets.QTreeWidget()
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet('background-color: rgb(99, 99, 99)')
        self.treeWidget.setMinimumSize(100, 100)
        self.treeWidget.setMaximumSize(QSize(250, 2000))
        self.treeWidget.header().setMinimumSectionSize(800)

        font = set_font()
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.left_box.addWidget(self.video_list_region)
        self.left_box.addWidget(self.treeWidget)
        self.horizontalLayout_5.addLayout(self.left_box)

        self.hor_right_layout = QtWidgets.QVBoxLayout()
        self.hor_right_layout.setObjectName("hor_right_layout")
        self.video_Frame1 = QtWidgets.QFrame(self.frame)
        self.video_Frame1.setMaximumSize(QtCore.QSize(1666666, 120))
        self.video_Frame1.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                          "color: rgb(255, 255, 255);")
        self.video_Frame1.setObjectName("video_Frame1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.video_Frame1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.video_player_region = QtWidgets.QLabel(self.video_Frame1)
        self.video_player_region.setObjectName("label")
        font = set_font(weight=70)
        self.video_player_region.setFont(font)
        self.horizontalLayout_6.addWidget(self.video_player_region)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.video_name = QtWidgets.QLabel(self.video_Frame1)
        self.video_name.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.video_name)
        self.hor_Spacer = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(self.hor_Spacer)
        self.btn_choose = QtWidgets.QPushButton('选择单个视频', self.video_Frame1)
        self.btn_choose.setObjectName("btn_choose")
        self.horizontalLayout_8.addWidget(self.btn_choose)
        self.btn_choose_videos = QtWidgets.QPushButton('批量导入视频', self.video_Frame1)
        self.btn_choose_videos.setObjectName("btn_choose_videos")
        self.horizontalLayout_8.addWidget(self.btn_choose_videos)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        
        self.hor_right_layout.addWidget(self.video_Frame1)
        self.video_widget = myVideoWidget()
        self.video_widget.setStyleSheet('background-color: rgb(75, 75, 75)')
        self.video_widget.setObjectName("widget")
        self.video_widget.setMinimumHeight(600)
        # self.gridLayout = QtWidgets.QGridLayout(self.video_widget)
        # self.gridLayout.setObjectName("gridLayout")
        self.hor_right_layout.addWidget(self.video_widget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
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
        self.lab_video.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.lab_video)
        self.lab_video_start = QtWidgets.QLabel(self.frame_2)
        self.lab_video_start.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.lab_video_start)
        self.horizontalLayout_9.addWidget(self.frame_2)
        self.hor_right_layout.addLayout(self.horizontalLayout_9)
        
        self.hor_btn_layout = QtWidgets.QHBoxLayout()
        self.hor_btn_layout.setObjectName("hor_btn_layout")
        
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(600, 70)
        self.frame_4.setStyleSheet("background-color: white;")
        # self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.hor_btn_left_layout = QtWidgets.QHBoxLayout(self.frame_4)
        self.hor_btn_left_layout.setObjectName("hor_btn_left_layout")
        self.quick_back = QtWidgets.QPushButton(self.frame_4)
        self.quick_back.setObjectName("quick_forward")
        self.hor_btn_left_layout.addWidget(self.quick_back)

        self.btn_play = QtWidgets.QPushButton(self.frame_4)
        self.btn_play.setObjectName("btn_play")
        self.hor_btn_left_layout.addWidget(self.btn_play)

        self.quick_forward = QtWidgets.QPushButton(self.frame_4)
        self.quick_forward.setObjectName("quick_forward")
        self.hor_btn_left_layout.addWidget(self.quick_forward)
        
        self.btn_stop = QtWidgets.QPushButton(self.frame_4)
        self.btn_stop.setObjectName("btn_stop")
        self.hor_btn_left_layout.addWidget(self.btn_stop)

        self.btn_video_list = QtWidgets.QPushButton(self.frame_4)
        self.btn_video_list.setObjectName("btn_video_list")
        self.hor_btn_left_layout.addWidget(self.btn_video_list)
        
        self.btn_close = QtWidgets.QPushButton(self.frame_4)
        self.btn_close.setObjectName("btn_close")
        self.hor_btn_left_layout.addWidget(self.btn_close)
        
        self.hor_btn_layout.addWidget(self.frame_4)
        
        self.hor_btn_Spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hor_btn_layout.addItem(self.hor_btn_Spacer)

        self.btn_voice = QtWidgets.QPushButton()
        self.btn_voice.setObjectName("btn_voice")
        self.hor_btn_layout.addWidget(self.btn_voice)

        self.voice_Slider = QSlider()
        self.voice_Slider.setMaximumSize(100, 20)
        self.voice_Slider.setValue(50)
        self.voice_Slider.setRange(0, 100)
        self.voice_Slider.setObjectName(u"voice_Slider")
        self.voice_Slider.setOrientation(Qt.Horizontal)
        self.hor_btn_layout.addWidget(self.voice_Slider)

        self.voice_video = QtWidgets.QLabel()
        self.voice_video.setObjectName('label')
        self.voice_video.setText('50%')
        self.voice_video.setMinimumWidth(50)
        self.hor_btn_layout.addWidget(self.voice_video)
        
        self.hor_right_layout.addLayout(self.hor_btn_layout)
        self.horizontalLayout_5.addLayout(self.hor_right_layout)
        
        self.verticalLayout_8.addWidget(self.frame)
        
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video"))
        self.video_player_region.setText(_translate("MainWindow", "视频播放区"))
        self.video_name.setText(_translate("MainWindow", "当前播放："))
        self.lab_video.setText(_translate("MainWindow", "|00:00"))
        self.lab_video_start.setText(_translate("MainWindow", "|00:00"))
        
        self.quick_back.setToolTip('left键 快退')
        self.quick_forward.setToolTip('right键 快进')
        self.voice_video.setStyleSheet('color: red')
        self.lab_video.setStyleSheet('color: yellow')
        self.lab_video_start.setStyleSheet('color: yellow')
        self.voice_video.setToolTip('up 增加 down 降低')
        
        
        btn_list = [self.btn_play, self.btn_stop, self.quick_back, self.quick_forward,
                    self.btn_video_list, self.btn_close]
        self.btn_play.setIcon(QIcon(static_base_path +  '\\static\\images\\stop.png')),
        self.btn_play.setToolTip("<p style='color: black'>播放/暂停 空格</p>")
        
        self.quick_back.setIcon(QIcon(static_base_path + '\\static\\images\\back.png')),
        self.quick_back.setToolTip("<p style='color: black'>快退5秒 left</p>")

        self.quick_forward.setIcon(QIcon(static_base_path + '\\static\\images\\forward.png'))
        self.quick_forward.setToolTip("<p style='color: black'>快进5秒 right</p>")

        self.btn_stop.setIcon(QIcon(static_base_path + '\\static\\images\\_stop.png'))
        self.btn_stop.setToolTip("<p style='color: black'>清屏 Ctrl + d</p>")

        self.btn_voice.setIcon(QIcon(static_base_path + '\\static\\images\\voice.png'))
        self.btn_voice.setToolTip("<p style='color: black'>音量</p>")

        self.btn_video_list.setIcon(QIcon(static_base_path + '\\static\\images\\video_list.png'))
        self.btn_video_list.setToolTip("<p style='color: white;'>隐藏/显示播放列表 Ctrl+W</p>")

        self.btn_close.setIcon(QIcon(static_base_path + '\\static\\images\\close.png'))
        self.btn_close.setToolTip("<p style='color: black'>退出程序Ctrl+R</p>")

        self.btn_choose.setToolTip("<p style='color: black'>Ctrl+g</p>")
        self.btn_choose_videos.setToolTip("<p style='color: black'>Ctrl+F</p>")

        self.btn_voice.setEnabled(False)
        QToolTip.setFont(QFont('Helvetica', 12))
        for item in btn_list:
            item.setMinimumWidth(70)
            item.setMinimumHeight(45)
            item.setIconSize(QSize(35, 35))

        self.btn_choose.setStyleSheet('background-color: rgb(139, 0, 0)')
        self.btn_choose_videos.setStyleSheet('background-color: rgb(139, 0, 0)')
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setHidden(True)

