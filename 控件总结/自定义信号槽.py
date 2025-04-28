import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        for i in range(100):
            self.progress.emit(i + 1)
        self.finished.emit()


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.button = QPushButton("Start", self)
        layout.addWidget(self.button)

        self.worker = Worker()
        self.worker.finished.connect(self.on_finished)
        self.worker.progress.connect(self.on_progress)

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