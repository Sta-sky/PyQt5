from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        # pte = QTextEdit(self)
        self.pte = pte
        pte.resize(300, 300)
        pte.move(100, 100)

        test_btn = QPushButton(self)
        test_btn.move(20, 20)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        # 展示行号
        line_num_parent = QWidget(self)
        line_num_parent.resize(30, 300)
        line_num_parent.move(70, 100)
        line_num_parent.setStyleSheet("background-color: cyan;")

        self.line_label = QLabel(line_num_parent)
        self.line_label.move(0, 6)

        # 1 - 100
        line_nums = "\n".join([str(i) for i in range(1, 101)])
        self.line_label.setText(line_nums)
        self.line_label.adjustSize()

        self.占位提示文本()
        # self.只读设置()
        self.格式设置()
        self.自动换行()
        self.覆盖模式()
        self.Tab控制()
        self.文本操作()
        self.pte.setCenterOnScroll(True)


    def btn_test(self):
        # self.块的操作()
        # self.放大缩小()
        self.光标操作()
        self.信号的操作()

        tc = QTextCursor(self.pte.document())
        tc.setPosition(6)
        tc.insertHtml("xxxxxx")




    def 信号的操作(self):
        self.pte.textChanged.connect(lambda :print("内容发生了改变"))
        self.pte.cursorPositionChanged.connect(lambda :print("光标位置改变"))
        self.pte.blockCountChanged.connect(lambda bc:print("块的个数改变", bc))
        self.pte.selectionChanged.connect(lambda :print("选中内容发生了改变", self.pte.textCursor().selectedText()))
        self.pte.modificationChanged.connect(lambda val:print("修改状态发生改变", val))
        doc = self.pte.document()
        doc.setModified(False)
        self.pte.updateRequest.connect(lambda rect, dy: self.line_label.move(self.line_label.x(), self.line_label.y() + dy))


    def 光标操作(self):
        QTextCursor
        # tc = self.pte.textCursor()
        # tc.insertImage("rose.png")
        # tc.insertTable(5, 6)
        # tc = self.pte.cursorForPosition(QPoint(20, 60))
        # print(tc)
        # tc.insertText("itlike")
        # self.pte.setCursorWidth(20)

        self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.pte.setFocus()

        pass

    def 滚动保证光标可见(self):
        # self.pte.centerCursor()
        self.pte.ensureCursorVisible()
        self.pte.setFocus()

    def 放大缩小(self):
        # self.pte.zoomIn(10)
        # self.pte.zoomIn(-1)
        self.pte.zoomOut(-10)

    def 块的操作(self):
        print(self.pte.blockCount())
        self.pte.setMaximumBlockCount(3)
        print(self.pte.toPlainText())

    def 文本操作(self):
        # self.pte.setPlainText("社会我顺哥, 人狠话不多")
        # self.pte.setPlainText("itlike.com")
        # self.pte.insertPlainText("itlike.com")
        # self.pte.appendPlainText("<a href='http://www.itlike.com'>撩课</a>")
        # self.pte.appendHtml("<a href='http://www.itlike.com'>撩课</a>")
        #
        # table_str = "<table border=2>" \
        #             "<tr><td>1</td><td>2</td><td>3</td></tr>" \
        #             "<tr><td>4</td><td>5</td><td>6</td></tr>" \
        #             "</table>"
        # # self.pte.setHtml(table_str)
        # self.pte.appendHtml(table_str)
        # print(self.pte.toPlainText())
        pass

    def Tab控制(self):
        self.pte.setTabChangesFocus(False)
        self.pte.setTabStopDistance(100)

    def 覆盖模式(self):
        print(self.pte.overwriteMode())
        self.pte.setOverwriteMode(True)
        print(self.pte.overwriteMode())

    def 自动换行(self):
        print(self.pte.lineWrapMode())
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)

    def 格式设置(self):
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(200, 100, 100))
        self.pte.setCurrentCharFormat(tcf)

    def 只读设置(self):
        self.pte.setReadOnly(True)
        print(self.pte.isReadOnly())

    def 占位提示文本(self):
        self.pte.setPlaceholderText("请输入你的个人信息")
        print(self.pte.placeholderText())
        pass
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.setWindowIcon(QIcon("bb.png"))
    window.show()


    sys.exit(app.exec_())