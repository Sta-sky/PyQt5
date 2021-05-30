from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QDialog
from PyQt5.QtGui import QIcon, QColor, QPainter, QPixmap
from PyQt5 import uic

class videoPlayer(QWidget):

    def __init__(self):
        super().__init__()
        # 播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.ui.wgt_player)
        # 按钮
        self.ui.btn_select.clicked.connect(self.open)
        self.ui.btn_play_pause.clicked.connect(self.playPause)
        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.ui.sld_duration.sliderMoved.connect(self.updatePosition)
        # 资源图片
        '''self.ui.btn_select.setIcon(QIcon('../icon/hide.png'))
        self.ui.btn_play_pause.setIcon(QIcon('../icon/play.png'))'''
        # self.ui.wgt_player.setStyleSheet("QWidget { background-color: QColor(0,0,0) }" )
        self.ui.btn_select.setStyleSheet('QPushButton{background:url(../icon/hide.png) no-repeat center}') # StyleSheet使用CSS语法
        self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
    # 打开视频文件
    def open(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()
        self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/pause.png) no-repeat center}')
    # 播放视频
    def playPause(self):
        if self.player.state()==1:
            self.player.pause()
            self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
        elif self.player.state()==2 or self.ui.sld_duration.value()!=0:
            self.player.play()
            self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/pause.png) no-repeat center}')
    # 视频总时长获取
    def getDuration(self, d):
        '''d是获取到的视频总时长（ms）'''
        self.ui.sld_duration.setRange(0, d)
        self.ui.sld_duration.setEnabled(True)
        self.displayTime(d)
    # 视频实时位置获取
    def getPosition(self, p):
        self.ui.sld_duration.setValue(p)
        self.displayTime(self.ui.sld_duration.maximum()-p)
    # 显示剩余时间
    def displayTime(self, ms):
        minutes = int(ms/60000)
        seconds = int((ms-minutes*60000)/1000)
        self.ui.lab_duration.setText('{}:{}'.format(minutes, seconds))
        if ms==0:
            self.ui.btn_play_pause.setStyleSheet('QPushButton{background:url(../icon/play.png) no-repeat center}')
    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.ui.sld_duration.maximum()-v)
    # 自定义paintEvent，绘制背景图
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.ui.rect(), QPixmap('../icon/bg_1.jpg'))

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('../icon/bupt.jpg'))
    myPlayer = videoPlayer()
    myPlayer.ui.show()
    app.exec()
