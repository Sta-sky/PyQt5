# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QLineEdit-功能测试")
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)
le.resize(300, 300)
# le.setContentsMargins(100, 0, 0, 0)
le.setStyleSheet("background-color: cyan;")
le.setTextMargins(0, 0, 50, 50)
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)
le.setDragEnabled(True)

le2 = QLineEdit(window)
le2.resize(50, 50)
le2.move(200, 0)

btn = QPushButton(window)
btn.setText("按钮")
btn.move(50, 50)
def cursor_move():
    # le.cursorBackward(True, 2)
    # le.cursorForward(True, 3)
    # le.cursorWordBackward(True)
    # le.cursorWordForward(True)
    # le.home(True)
    # le.end(False)
    # le.setCursorPosition(len(le.text()) / 2)
    # le.setCursorPosition(1.5)
    # print(le.cursorPosition())
    # print(le.cursorPositionAt(QPoint(55, 105)))
    # le.setText("社会我顺哥"*10)
    # le.home(False)
    # le.setFocus()
    # le.cursorBackward(True, 2)
    # le.backspace()
    # le.del_()
    # le.clear()
    # le.setText("")
    # le.setFocus()

    # le.cursorBackward(True, 3)
    # # le.copy()
    # le.cut()
    # le.setCursorPosition(0)
    # le.paste()


    # le.setSelection(2, 21)
    # le.selectAll()
    # le.setSelection(0, len(le.text()))
    # le.deselect()
    le.setSelection(2, 3)
    print(le.hasSelectedText())

    print(le.selectedText())
    print(le.selectionStart())
    print(le.selectionEnd())
    print(le.selectionLength())
    pass


btn.clicked.connect(cursor_move)


le.textEdited.connect(lambda val: print("文本框编辑的时候", val))
le.textChanged.connect(lambda val: print("文本框内容发生改变", val))

# le.returnPressed.connect(lambda :print("回车键被按下"))
# le.returnPressed.connect(lambda :le2.setFocus())
# le.editingFinished.connect(lambda :print("结束编辑"))


# le.cursorPositionChanged.connect(lambda old_Pos, new_Pos: print(old_Pos, new_Pos))
le.selectionChanged.connect(lambda : print("选中文本发生改变", le.selectedText()))

le.setText("xxx")

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())