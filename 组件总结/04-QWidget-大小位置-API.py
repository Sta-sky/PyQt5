# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

window = QWidget()
window.move(200, 100)
window.resize(500, 500)
# window.setFixedSize(500, 500)


label = QLabel(window)
label.setText("社会顺")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")

def changeCao():
    new_content = label.text() + "社会顺"
    label.setText(new_content)

    # label.resize(label.width() + 100, label.height())
    label.adjustSize()


btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100, 300)
btn.clicked.connect(changeCao)


# window.setGeometry(0, 0, 150, 150)

# print(window.x())
# print(window.width())
# print(window.geometry())

window.show()
# window.setGeometry(0, 0, 150, 150)

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())