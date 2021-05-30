from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.setStyleSheet("background-color: rgb(100, 200, 150);")
        # QColorDialog.setCustomColor(3, QColor(100, 200, 50))
        # QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        # cd = QColorDialog(QColor(100, 200, 150), self)
        # cd.setWindowTitle("选择一个好看的颜色")
        # def color():
        #
        #     print(cd.customCount())
        #     cd.setCustomColor(0, QColor(200, 100, 20))
        #     return None
        #     palette = QPalette()
        #     # palette.setColor(QPalette.Background, cd.selectedColor())
        #     palette.setColor(QPalette.Background, cd.currentColor())
        #     self.setPalette(palette)
        # # cd.colorSelected.connect(color)
        # cd.currentColorChanged.connect(color)
        # cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        # cd.show()


        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")

        def test():
            cd = QColorDialog(self)
            cd.setOption(QColorDialog.NoButtons)
            cd.setWindowTitle("选择一个人生的颜色")

            def sel_color(color):
                palette = QPalette()
                palette.setColor(QPalette.ButtonText, color)
                btn.setPalette(palette)
                pass
            # cd.colorSelected.connect(sel_color)
            cd.currentColorChanged.connect(sel_color)

            cd.show()

            # color = QColorDialog.getColor(QColor(10, 20, 100), self, "选择颜色")
            # palette = QPalette()
            # # palette.setColor(QPalette.Background, cd.selectedColor())
            # palette.setColor(QPalette.Background, color)
            # self.setPalette(palette)
            # print(color)
        btn.clicked.connect(test)

        # btn.clicked.connect(lambda :print(QColorDialog.customCount()))

        # cd.open(color)
        # if cd.exec():
        #     color()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())