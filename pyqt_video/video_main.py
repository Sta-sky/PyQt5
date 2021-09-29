# -*- coding: utf-8 -*-
# 主函数文件。syswin.py
import os
import sys

from PyQt5.QtCore import QUrl, QSize, Qt, QRectF, QRect
from PyQt5.QtGui import QIcon, QKeySequence, QPainterPath, QColor, QPainter, QBrush
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem, QShortcut, qApp, QMessageBox

from utils import echo
from video_ui import Ui_MainWindow


class VideoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.desktop = QApplication.desktop()
        self.desktop_width = self.desktop.width() * 0.8
        self.desktop_height = self.desktop.height() * 0.7
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(int(self.desktop_width), int(self.desktop_height))
        self.move(200, 100)
        self.base_path_list = []
        self.move_flag = False
        self.start_x = 0
        self.start_y = 0
        self.static_base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))
        # self.static_base_path = '.'
        ico_path = self.static_base_path + '\\static\\images\\video.png'
        self.setWindowIcon(QIcon(ico_path))
        qss_path = self.static_base_path + '\\static\\qss\\style.qss'
        with open(qss_path, 'r') as fp:
            self.setStyleSheet(fp.read())
        self.setAutoFillBackground(False)
        self.border_width = 8

        # 设置播放暂停的标志
        self.FLAG_PLAY = False
        
        # 视频操作  # 定义player
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)  # 视频播放输出的widget，就是上面定义的
        self.player.positionChanged.connect(self.changeSlide)  # 位置改变触发，设置进度
        self.player.durationChanged.connect(self.getprocess)   # 时间改变后触发设置时间进度
        self.btn_video_list.clicked.connect(self.video_list_show)
        self.sld_video.sliderMoved.connect(self.updatePosition)
        self.voice_Slider.sliderMoved.connect(self.voice_update)
        self.video_list = qApp.arguments()
        if len(self.video_list) > 1:
            self.curr_video = self.video_list[1]
            if os.path.exists(self.curr_video):
                self.curr_play_video()
            else:
                echo(self, '路径不存在')
        
        # 快捷键控制进度
        QShortcut(QKeySequence('Left'), self, self.key_video_back)
        QShortcut(QKeySequence('Right'), self, self.key_video_forward)
        QShortcut(QKeySequence('Up'), self, self.voice_big)
        QShortcut(QKeySequence('Down'), self, self.voice_small)
        QShortcut(QKeySequence('Space'), self, self.playVideo)
        QShortcut(QKeySequence("Ctrl+R"), self, self.key_close)
        QShortcut(QKeySequence("Ctrl+D"), self, self.key_clear_video)
        QShortcut(QKeySequence("Ctrl+G"), self, self.file_video)
        QShortcut(QKeySequence("Ctrl+F"), self, self.files_video)
        QShortcut(QKeySequence("Ctrl+W"), self, self.show_list)
        QShortcut(QKeySequence("Esc"), self, self.handle_esc)
        QShortcut(QKeySequence("Ctrl+Alt+Z"), self, self.hide_window)
        
        # 这里进行按钮的绑定
        self.btn_choose.clicked.connect(self.open_video_file)
        self.btn_choose_videos.clicked.connect(self.choose_videos_tree)
        self.btn_play.clicked.connect(self.playVideo)
        self.btn_stop.clicked.connect(self.stopVideo)
        self.btn_close.clicked.connect(self.close)
        self.video_widget.doubleClickedItem.connect(self.videoDoubleClicked)
        self.btn_min.clicked.connect(self.hide_window)
        
        # 控制音量
        self.player.setVolume(50)
        self.video_widget.wheelItem.connect(self.handle_voice)
        self.treeWidget.clicked.connect(self.handle_click_video)
        self.quick_forward.clicked.connect(self.video_forward)
        self.quick_back.clicked.connect(self.video_back)

    def paintEvent(self, event):
        # 阴影
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        pat = QPainter(self)
        pat.setRenderHint(pat.Antialiasing)
        pat.fillPath(path, QBrush(Qt.white))
        color = QColor(192, 192, 192, 50)
        for i in range(10):
            i_path = QPainterPath()
            i_path.setFillRule(Qt.WindingFill)
            ref = QRectF(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2)
            i_path.addRoundedRect(ref, self.border_width, self.border_width)
            color.setAlpha(150 - i ** 0.5 * 50)
            pat.setPen(color)
            pat.drawPath(i_path)
        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        pat2.setBrush(Qt.white)
        pat2.setPen(Qt.transparent)
        rect = self.rect()
        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width() - 9) # 控制水平偏移量
        rect.setHeight(rect.height() - 9) # 控制竖直偏移量
        pat2.drawRoundedRect(rect, 10, 10) # 控制圆角锐度

    def curr_play_video(self):
        try:
            video_name = os.path.split(self.curr_video)[1]
            self.video_name.setText(f'当前播放视频为： {video_name}')
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.curr_video)))  # 选取视频文件
            self.player.play()  # 播放视频
            self.FLAG_PLAY = True
            self.btn_play.setIcon(QIcon(self.static_base_path + '\\static\\images\\player.png'))
        except Exception as e:
            return
    
    def voice_update(self, v):
        if not v:
            return
        self.player.setVolume(v)
        self.voice_video.setText(f'{v}%')

    def handle_voice(self, wheel_size):
        try:
            self.voice_Slider.show()
            voice_size = self.player.volume()
            wheel_size = int(wheel_size)
            if wheel_size < 0:
                if voice_size <= 0:
                    return
                else:
                    voice_size -= 5
            if wheel_size > 0:
                if voice_size >= 100:
                    return
                else:
                    voice_size += 5
            self.player.setVolume(voice_size)
            voice = self.player.volume()
            self.voice_Slider.setValue(voice)
            self.voice_video.setText(f'{voice}%')
        except Exception as e:
            echo(self, str(e))
            return
            
    def video_forward(self):
        forward_position = self.player.position() + 5000
        if forward_position == 5000:
            return
        if forward_position > self.sld_video.maximum():
            forward_position = self.sld_video.maximum()
        self.player.setPosition(forward_position)
        self.displayTime(forward_position)
    
    def key_video_forward(self):
        self.quick_forward.animateClick(50)
    
    def key_video_back(self):
        self.quick_back.animateClick(50)
    
    def video_back(self):
        back_position = self.player.position() - 5000
        if back_position == -5000:
            return
        if back_position < 0:
            back_position = 0
        self.player.setPosition(back_position)
        self.displayTime(back_position)
    
    def key_clear_video(self):
        self.btn_stop.animateClick(50)
        
    def file_video(self):
        self.btn_choose.animateClick(50)
    
    def files_video(self):
        self.btn_choose_videos.animateClick(50)

    def voice_big(self):
        voice_size = self.player.volume()
        if voice_size >= 100:
            return
        else:
            voice_size += 5
            self.player.setVolume(voice_size)
            self.voice_video.setText(f'{voice_size}%')
            self.voice_Slider.setValue(voice_size)

    def voice_small(self):
        voice_size = self.player.volume()
        if voice_size <= 0:
            return
        else:
            voice_size -= 5
            self.player.setVolume(voice_size)
            self.voice_video.setText(f'{voice_size}%')
            self.voice_Slider.setValue(voice_size)
    
    def getprocess(self, total_time):
        """total_time 当前总时长"""
        self.sld_video.setRange(0, total_time)
        self.sld_video.setEnabled(True)
        minutes = int(total_time / 60000)
        seconds = int((total_time - minutes * 60000) / 1000)
        self.lab_video_start.setText(' | {}:{}'.format(minutes, seconds))
    
    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(v)
    
    def handle_click_video(self):
        try:
            video_name = self.treeWidget.selectedItems()[0].text(0)
            item = self.treeWidget.currentItem().parent()
            if not item:
                return
            current_node_index = self.treeWidget.indexOfTopLevelItem(item)
            self.base_path = self.base_path_list[current_node_index]
            video_path = f'{self.base_path}/{video_name}'
            self.curr_video = video_path
            self.video_name.setText(f'当前播放视频为： {video_name}')
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.curr_video)))  # 选取视频文件
            self.player.play()  # 播放视频
            self.FLAG_PLAY = True
            self.btn_play.setIcon(QIcon(self.static_base_path + '\\static\\images\\player.png'))
        except Exception as e:
            print(e)
            return
    
    def choose_videos_tree(self):
        try:
            self.base_path = ''
            result1 = QFileDialog.getOpenFileNames(self, '选择视频', 'c:/', '所有(*.*)')
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
    
    def open_video_file(self):
        try:
            file = QFileDialog.getOpenFileUrl()[0]
            if not file.fileName():
                return
            self.curr_video = file
            self.video_name.setText(f'当前播放视频为： {file.fileName()}')
            self.player.setMedia(QMediaContent(self.curr_video))  # 选取视频文件
            self.player.play()  # 播放视频
            self.FLAG_PLAY = True
        except Exception as e:
            return
    
    def video_list_show(self):
        if self.treeWidget.isHidden():
            self.video_list_region.show()
            self.treeWidget.show()
        else:
            self.video_list_region.hide()
            self.treeWidget.hide()
        
    def show_list(self):
        self.btn_video_list.animateClick(50)
    
    def playVideo(self):
        # 如果没有播放，则进行播放
        if not self.FLAG_PLAY:
            self.btn_play.setIcon(QIcon(self.static_base_path + '\\static\\images\\player.png'))
            self.player.play()
            self.FLAG_PLAY = True
        else:
            self.btn_play.setIcon(QIcon(self.static_base_path + '\\static\\images\\stop.png'))
            self.player.pause()
            self.FLAG_PLAY = False
        self.btn_play.setIconSize(QSize(40, 40))
    
    def stopVideo(self):
        self.player.stop()
        self.btn_play.setIcon(QIcon(self.static_base_path + '\\static\\images\\stop.png'))
        self.btn_play.setIconSize(QSize(40, 40))

    def changeSlide(self, position):
        self.sld_video.setValue(position)
        self.displayTime(position)
    
    def displayTime(self, ms):
        minutes = int(ms / 60000)
        seconds = int((ms - minutes * 60000) / 1000)
        self.lab_video.setText('{}:{}'.format(minutes, seconds))
    
    def handle_esc(self):
        if self.video_widget.isFullScreen():
            self.video_widget.setFullScreen(0)
            self.video_widget.setMaximumSize(self.wsize)
    
    def hide_window(self):
        if self.isHidden():
            self.show()
        else:
            self.showMinimized()

    def videoDoubleClicked(self):
        if self.player.duration() > 0:  # 开始播放
            if self.video_widget.isFullScreen():
                self.video_widget.setFullScreen(False)
                self.video_widget.setMaximumSize(self.wsize)
            else:
                self.wsize = self.video_widget.size()
                self.video_widget.setFullScreen(True)
                self.raise_()

    def key_close(self):
        self.btn_close.animateClick(50)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '你确认要退出吗？', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.move_flag = True
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseMoveEvent(self, event):  # 重写移动事件
        if self.move_flag:
            label_x = event.globalPos().x()
            label_y = event.globalPos().y()
            start = label_x - self.start_x
            end = label_y - self.start_y
            self.move(start, end)
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = VideoWindow()
    main_window.show()
    sys.exit(app.exec_())
