from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # result = QFileDialog.getOpenFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getOpenFileNames(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getOpenFileUrl(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getSaveFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getExistingDirectory(self, "选择一个py文件", "./")
        # result = QFileDialog.getExistingDirectoryUrl(self, "选择一个py文件", QUrl("./"))
        # print(result)

        def test():
            fd = QFileDialog(self, "选择一个文件", "../", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")

            # fd.fileSelected.connect(lambda file: print(file))

            # fd.setAcceptMode(QFileDialog.AcceptSave)
            # fd.setDefaultSuffix("txt")

            # fd.setFileMode(QFileDialog.Directory)
            # fd.setNameFilter("IMG(*.jpg *.png *.jpeg)")
            # fd.setNameFilters(["All(*.*)", "Images(*.png *.jpg)", "Python文件(*.py)"])

            # fd.setViewMode(QFileDialog.Detail)
            fd.setLabelText(QFileDialog.FileName, "顺哥的文件")
            fd.setLabelText(QFileDialog.Accept, "顺哥的接受")
            fd.setLabelText(QFileDialog.Reject, "顺哥的拒绝")

            # fd.currentChanged.connect(lambda path: print("当前路径字符串发生改变时", path))
            # fd.currentUrlChanged.connect(lambda url: print("当前路径QUrl发生改变时", url))
            # fd.directoryEntered.connect(lambda path: print("当前目录字符串进入时", path))
            # fd.directoryUrlEntered.connect(lambda url: print("当前目录QUrl进入时", url))
            # fd.filterSelected.connect(lambda filter: print("当前名称过滤字符串被选中时", filter))
            fd.setFileMode(QFileDialog.ExistingFiles)
            fd.fileSelected.connect(lambda val:print("单个文件被选中-字符串", val))
            fd.filesSelected.connect(lambda val:print("多个文件被选中-列表[字符串]", val))
            fd.urlSelected.connect(lambda val:print("单个文件被选中-url", val))
            fd.urlsSelected.connect(lambda val:print("多个文件被选中-列表[url]", val))


            fd.open()

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100, 100)
        btn.clicked.connect(test)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())