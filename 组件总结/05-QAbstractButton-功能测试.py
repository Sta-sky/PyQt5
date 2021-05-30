# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("按钮的功能测试-抽象类")
window.resize(500, 500)

# btn = QPushButton(window)


# *************文本操作***************开始
# btn.setText("1")
# def plus_one():
#     print("加一")
#     num = int(btn.text()) + 1
#     btn.setText(str(num))
#
# btn.pressed.connect(plus_one)
# *************文本操作***************结束

# *************图标操作***************开始

# icon = QIcon("xxx.png")
# btn.setIcon(icon)
#
# size = QSize(50, 50)
# btn.setIconSize(size)
#
# print(btn.icon())
# print(btn.iconSize())

# *************图标操作***************结束


# *************快捷键的设定***************开始

# btn.pressed.connect(lambda :print("按钮被点击了"))
# # btn.setText("a&bc")
# btn.setShortcut("Alt+a")


# *************快捷键的设定***************结束


# *************自动重复***************开始
# btn.setAutoRepeat(True)
# btn.setAutoRepeatDelay(2000)
# btn.setAutoRepeatInterval(1000)
# print(btn.autoRepeat())
# print(btn.autoRepeatInterval())
# print(btn.autoRepeatDelay())

# *************自动重复***************结束

# *************按钮状态***************开始
# push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100, 100)
#
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100, 150)
#
# checkbox = QCheckBox(window)
# checkbox.setText("这是checkbox")
# checkbox.move(100, 200)
#
# push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")
#
# # 把三个按钮, 置为按下状态
# # push_button.setDown(True)
# # radio_button.setDown(True)
# # checkbox.setDown(True)
# push_button.setCheckable(True)
# print(push_button.isCheckable())
# print(radio_button.isCheckable())
# print(checkbox.isCheckable())
#
# radio_button.setChecked(True)
# push_button.setChecked(True)
# checkbox.setChecked(True)
#
# print(push_button.isChecked())
# print(radio_button.isChecked())
# print(checkbox.isChecked())
#
# def cao():
#     push_button.toggle()
#     radio_button.toggle()
#     checkbox.toggle()
#
#     # push_button.setChecked(not push_button.isChecked())
#
#
# btn.pressed.connect(cao)
#
#
# push_button.setEnabled(False)
# radio_button.setEnabled(False)
# checkbox.setEnabled(False)

# *************按钮状态***************结束











# 2.3 展示控件

# *************排他性设置***************开始

# for i in range(0, 3):
#     btn = QCheckBox(window)
#     btn.setText("btn" + str(i))
#     btn.move(50 * i, 50 * i)
#
#     btn.setAutoExclusive(True)
#     print(btn.autoExclusive())
#     print(btn.isCheckable())
    # btn.setCheckable(True)


# *************排他性设置***************结束

# *************按钮模拟点击***************开始

# btn = QPushButton(window)
# btn.setText("这是按钮")
# btn.move(200, 200)
# btn.pressed.connect(lambda :print("点击了这个按钮"))


# btn.click()

# btn.animateClick(2000)


# btn2 = QPushButton(window)
# btn2.setText("按钮2")
# def test():
#     # btn.click()
#     btn.animateClick(1000)
# btn2.pressed.connect(test)


# *************按钮模拟点击***************结束

class Btn(QPushButton):
    def hitButton(self, point):
        # print(point)
        # if point.x() > self.width() / 2:
        #     return True
        # return False

        # 通过给定的一个点坐标, 计算与圆心的距离
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # ((x1 - x2) 平方 + (y1 - y2) 平方) 开平方
        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))
        if distance < self.width() / 2:
            return True

        # 如果距离 < 半径  True
        # 返回 False
        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))
        painter.drawEllipse(self.rect())

btn = Btn(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)
btn.setCheckable(True)
btn.pressed.connect(lambda : print("按钮被按下了"))

btn.released.connect(lambda : print("按钮鼠标被释放了"))

btn.clicked.connect(lambda value: print("按钮被点击", value))

btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))


window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())