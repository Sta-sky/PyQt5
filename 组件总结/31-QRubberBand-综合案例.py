from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0, 添加子控件, 复选框
        for i in range(0, 30):
            cb = QCheckBox(self)
            cb.setText("{}".format(i))
            cb.move(i % 4 * 50, i // 4 * 60)

        # 1. 创建一个橡皮筋选中控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt):
        QMouseEvent

        # 2. 尺寸大小 : 鼠标点击的位置点 , 00
        self.origin_pos = evt.pos()
        self.rb.setGeometry(QRect(self.origin_pos, QSize()))
        # 3. 展示橡皮筋控件
        self.rb.show()
        pass
    def mouseMoveEvent(self, evt):
        # 调整橡皮筋选中控件的位置以及尺寸
        self.rb.setGeometry(QRect(self.origin_pos, evt.pos()).normalized())
        pass

    def mouseReleaseEvent(self, evt):
        # 1. 获取橡皮筋控件的尺寸范围
        rect = self.rb.geometry()
        # 2. 遍历所有的子控件, 查看, 哪些子控件在区域范围
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                # print(child)
                child.toggle()
        self.rb.hide()
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())