import sys
from PyQt5.Qt import *


app = QApplication(sys.argv)

window = QWidget()



window.show()
window.resize(500, 500)
window.move(300, 300)

# 总的控件个数
widget_count = 100
# 一行有多少列
column_count = 3

# 计算一个控件的宽度
widget_width = window.width() / column_count
# 总共有多少行 (编号 // 一行多少列 + 1)
row_count = (widget_count - 1) // column_count + 1
widget_height = window.height() / row_count

for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x, widget_y)
    w.setStyleSheet("background-color: red;border: 1px solid yellow;")
    w.show()

sys.exit(app.exec_())