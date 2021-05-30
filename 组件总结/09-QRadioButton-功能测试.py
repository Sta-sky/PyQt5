# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QRadioButton-功能测试")
window.resize(500, 500)


red = QWidget(window)
red.resize(200, 200)
red.setStyleSheet("background-color: red;")
red.move(50, 50)

green = QWidget(window)
green.resize(200, 200)
green.setStyleSheet("background-color: green;")
green.move(red.x() + red.width(), red.y() + red.height())

rb_nan = QRadioButton("男", red)
rb_nan.setShortcut("Alt+M")
rb_nan.move(10, 10)
rb_nan.setChecked(True)

rb_nv = QRadioButton("女-&Female", red)
rb_nv.move(10, 50)
rb_nv.setIcon(QIcon("xxx.png"))
# rb_nv.setIconSize(QSize(60, 60))
rb_nv.toggled.connect(lambda isChecked: print(isChecked))

# rb_nv.setAutoExclusive(False)

rb_yes = QRadioButton("yes", green)
rb_yes.move(10, 10)
rb_no = QRadioButton("no", green)
rb_no.move(10, 50)



# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())