# -*- coding: utf-8 -*-
# 主函数文件。syswin.py

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QShortcut
from PyQt5.QtMultimedia import *

from utils import echo
from video_ui import Ui_MainWindow


class Car_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(1700, 900)
        self.base_path_list = []
        self.setWindowIcon(QIcon('./video.png'))
        # 设置播放暂停的标志
        self.FLAG_PLAY = False
        self.videoFullScreen = False  # 判断当前widget是否全屏
        # 视频操作  		# 定义player
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)  # 视频播放输出的widget，就是上面定义的
        self.player.positionChanged.connect(self.changeSlide)  # 位置改变触发，设置进度
        self.player.durationChanged.connect(self.getprocess)         # 时间改变后触发设置时间进度
        self.sld_video.sliderMoved.connect(self.updatePosition)

        # 这里进行按钮的绑定
        self.btn_choose.clicked.connect(self.openVideoFile)
        self.btn_play.clicked.connect(self.playVideo)
        self.btn_stop.clicked.connect(self.stopVideo)
        self.widget.doubleClickedItem.connect(self.videoDoubleClicked)
        self.btn_choose_videos.clicked.connect(self.choose_videos_tree)
        self.treeWidget.clicked.connect(self.handle_click_video)
        self.quick_forward.clicked.connect(self.video_forward)
        self.quick_back.clicked.connect(self.video_back)

        # 快捷键控制进度
        self.quick_left = QShortcut(QKeySequence('Left'), self)
        self.quick_right = QShortcut(QKeySequence('Right'), self)
        self.quick_space = QShortcut(QKeySequence('Space'), self)

        self.quick_left.activated.connect(self.video_back)
        self.quick_right.activated.connect(self.video_forward)
        self.quick_space.activated.connect(self.playVideo)

    def video_forward(self):
        forward_position = self.player.position() + 5000
        if forward_position == 5000:
            echo(self, '请添加文件')
            return
        if forward_position > self.sld_video.maximum():
            forward_position = self.sld_video.maximum()
        self.player.setPosition(forward_position)
        self.displayTime(self.sld_video.maximum() - forward_position)

    def video_back(self):
        back_position = self.player.position() - 5000
        if back_position == -5000:
            echo(self, '请添加文件')
            return
        if back_position < 0:
            back_position = 0
        self.player.setPosition(back_position)
        self.displayTime(self.sld_video.maximum() - back_position)

    def getprocess(self, total_time):
        """total_time 当前总时长"""
        self.sld_video.setRange(0, total_time)
        self.sld_video.setEnabled(True)
        self.displayTime(total_time)

    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.sld_video.maximum() - v)

    def handle_click_video(self):
        try:
            video_name = self.treeWidget.selectedItems()[0].text(0)
            item = self.treeWidget.currentItem().parent()
            if not item:
                return
            current_node_index = self.treeWidget.indexOfTopLevelItem(item)
            self.base_path = self.base_path_list[current_node_index]
            video_path = f'{self.base_path}/{video_name}'
            self.video_name.setText(f'当前播放视频为： {video_name}')
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))  # 选取视频文件
            self.player.play()  # 播放视频
            self.FLAG_PLAY = True
        except Exception as e:
            return

    def choose_videos_tree(self):
        try:
            self.base_path = ''
            result1 = QFileDialog.getOpenFileNames(
                self, '选择视频', 'c:/', '所有(*.mp4 *.wmv *.AVI *.MOV *.3GP *.mp3);;图片(*.png *.jpg *.jfif)')
            base_path = result1[0][0].split('/')
            img_list = result1[0]
            base_path.pop()
            for i in base_path:
                self.base_path = self.base_path + f'{i}/'
            self.base_path_list.append(self.base_path)
            root_file = QTreeWidgetItem(self.treeWidget)
            root_file.setText(0, self.base_path)
            for img in img_list:
                img = img.split('/')[-1]
                child = QTreeWidgetItem(root_file)
                child.setText(0, img)
        except Exception as e:
            return

    def openVideoFile(self):
        try:
            file = QFileDialog.getOpenFileUrl()[0]
            file_flag = str(file).split('(')[-1]
            if len(file_flag) < 4:
                return
            video_name = str(file).split('/')[-1].replace(')', '')
            self.video_name.setText(f'当前播放视频为： {video_name}')
            self.player.setMedia(QMediaContent(file))  # 选取视频文件
            self.player.play()  # 播放视频
            self.FLAG_PLAY = True
        except Exception as e:
            return

    def playVideo(self):
        # 如果没有播放，则进行播放
        if not self.FLAG_PLAY:
            self.player.play()
            self.FLAG_PLAY = True
        else:
            self.player.pause()
            self.FLAG_PLAY = False

    def stopVideo(self):
        self.player.stop()

    def changeSlide(self, position):
        self.sld_video.setValue(position)
        self.displayTime(self.sld_video.maximum() - position)

    def displayTime(self, ms):
        minutes = int(ms / 60000)
        seconds = int((ms - minutes * 60000) / 1000)
        self.lab_video.setText('{}:{}'.format(minutes, seconds))

    def videoDoubleClicked(self, text):
        if self.player.duration() > 0:  # 开始播放
            # 后才允许进行全屏操作
            if self.videoFullScreen:
                self.videoFullScreen = False
                self.widget.setFullScreen(0)
                self.widget.setMaximumSize(self.wsize)
            else:
                self.wsize = self.widget.size()
                self.widget.setFullScreen(1)
                self.videoFullScreen = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Car_window()
    main_window.show()
    sys.exit(app.exec_())
