# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QSlider, QAction, QSplitter, QGroupBox, \
    QToolTip, QStatusBar, QWidget

from utils import set_font
from video_win import myVideoWidget

static_base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
# static_base_path = '.'


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.outlogin = QAction(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ver_win_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.ver_win_layout.setObjectName("ver_win_layout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.hor_left_right_layout = QtWidgets.QHBoxLayout(self.frame)
        self.hor_left_right_layout.setContentsMargins(1, 1, 1, 1)
        self.hor_left_right_layout.setObjectName("hor_left_right_layout")
        
        self.left_box = QVBoxLayout()
        font = set_font(weight=70)
        self.video_list_region = QLabel('视频播放列表')
        self.video_list_region.setObjectName('label')
        self.video_list_region.setFont(font)
        self.treeWidget = QtWidgets.QTreeWidget()
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet('background-color: rgb(99, 99, 99)')
        self.treeWidget.setMaximumWidth(250)
        self.treeWidget.header().setMinimumSectionSize(800)

        font = set_font()
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.left_box.addWidget(self.video_list_region)
        self.left_box.addWidget(self.treeWidget)
        self.hor_left_right_layout.addLayout(self.left_box)
        
        # 右边布局开始
        self.hor_right_layout = QtWidgets.QVBoxLayout()
        self.hor_right_layout.setObjectName("hor_right_layout")
        
        # 视频信息 frame 布局
        self.video_info_frame = QtWidgets.QFrame(self.frame)
        self.video_info_frame.setMaximumHeight(80)
        self.video_info_frame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                          "color: rgb(255, 255, 255);")
        self.video_info_frame.setObjectName("video_Frame1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.video_info_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.video_player_region = QtWidgets.QLabel(self.video_info_frame)
        self.video_player_region.setObjectName("label")
        font = set_font(weight=70)
        self.video_player_region.setFont(font)
        self.horizontalLayout_6.addWidget(self.video_player_region)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.video_name = QtWidgets.QLabel(self.video_info_frame)
        self.video_name.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.video_name.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.video_name)
        self.hor_Spacer = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(self.hor_Spacer)
        self.btn_choose = QtWidgets.QPushButton('选择单个视频', self.video_info_frame)
        self.btn_choose.setObjectName("btn_choose")
        self.horizontalLayout_8.addWidget(self.btn_choose)
        self.btn_choose_videos = QtWidgets.QPushButton('批量导入视频', self.video_info_frame)
        self.btn_choose_videos.setObjectName("btn_choose_videos")
        self.horizontalLayout_8.addWidget(self.btn_choose_videos)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.hor_right_layout.addWidget(self.video_info_frame)
        
        # 视频布局 frame 开始
        self.hor_video_layout = QtWidgets.QVBoxLayout(self.frame)
        self.hor_video_layout.setStretch(1, 100)
        self.video_widget = myVideoWidget()
        self.video_widget.setStyleSheet('background-color: rgb(75, 75, 75)')
        self.hor_video_layout.addWidget(self.video_widget)
        self.hor_right_layout.addLayout(self.hor_video_layout)
        
        # 进度条布局 frame 开始
        self.frame_2 = QtWidgets.QFrame()
        self.frame_2.setMaximumHeight(60)
        self.frame_2.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hor_slider_layout = QtWidgets.QHBoxLayout(self.frame_2)
        self.hor_slider_layout.setObjectName("hor_slider_layout")
        self.sld_video = QtWidgets.QSlider(self.frame_2)
        self.sld_video.setMaximumHeight(100)
        with open(static_base_path + '\\static\\qss\\slider.qss') as fp:
            self.sld_video.setStyleSheet(fp.read())
        self.sld_video.setPageStep(5)
        self.sld_video.setTracking(True)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.hor_slider_layout.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.frame_2)
        self.lab_video.setObjectName("label")
        self.hor_slider_layout.addWidget(self.lab_video)
        self.lab_video_start = QtWidgets.QLabel(self.frame_2)
        self.lab_video_start.setObjectName("label")
        
        self.hor_slider_layout.addWidget(self.lab_video_start)
        self.hor_right_layout.addWidget(self.frame_2)

        # 按钮布局 frame 开始
        self.hor_btn_layout = QtWidgets.QHBoxLayout(self.frame)
        self.hor_btn_layout.setObjectName("hor_btn_layout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumHeight(70)
        self.frame_4.setStyleSheet("background-color: white;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
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
        
        self.btn_min = QtWidgets.QPushButton(self.frame_4)
        self.btn_min.setObjectName("btn_min")
        self.hor_btn_left_layout.addWidget(self.btn_min)
        
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
        self.voice_video.setMaximumSize(50, 50)
        self.hor_btn_layout.addWidget(self.voice_video)
        
        self.hor_right_layout.addLayout(self.hor_btn_layout)
        self.hor_left_right_layout.addLayout(self.hor_right_layout)
        
        self.ver_win_layout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
                    self.btn_video_list, self.btn_close, self.btn_min]
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
        
        self.btn_min.setIcon(QIcon(static_base_path + '\\static\\images\\min.png'))
        self.btn_min.setToolTip("<p style='color: black'>Ctrl+Alt+Z</p>")

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

