import sys
import time

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QProgressBar


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, progress_bar):
        super().__init__()
        self.progress_bar = progress_bar  # 传入主窗口中的进度条

    def run(self):
        self.progress_bar.setRange(0, 100)  # 设置进度条范围
        for i in range(100):
            self.progress.emit(i + 1)  # 发射进度信号
            self.progress_bar.setValue(i + 1)  # 更新进度条的值
            QApplication.processEvents()  # 强制刷新界面
            time.sleep(0.1)  # 模拟耗时操作
        self.finished.emit()  # 发射完成信号


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(400, 200)  # 调整主窗口大小

    def initUI(self):
        layout = QVBoxLayout(self)  # 创建垂直布局

        # 创建按钮
        self.button = QPushButton("Start", self)
        layout.addWidget(self.button)

        # 创建进度条并添加到布局中
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # 初始化 Worker，并传入进度条
        self.worker = Worker(self.progress_bar)
        self.worker.finished.connect(self.on_finished)
        self.worker.progress.connect(self.on_progress)

        # 按钮点击时启动任务
        self.button.clicked.connect(self.worker.run)

    def on_finished(self):
        print("Task finished!")

    def on_progress(self, progress):
        print(f"Progress: {progress}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec_())