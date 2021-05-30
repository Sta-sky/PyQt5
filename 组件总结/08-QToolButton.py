# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QToolButton使用")
window.resize(500, 500)

tb = QToolButton(window)
# tb = QPushButton(window)
tb.setText("工具")
tb.setIcon(QIcon("xxx.png"))
# tb.setIconSize(QSize(60, 60))
# tb.setToolTip("这是一个新建按钮")
# Qt.ToolButtonIconOnly
# 	仅显示图标
# Qt.ToolButtonTextOnly
# 	仅显示文字
# Qt.ToolButtonTextBesideIcon
# 	文本显示在图标旁边
# Qt.ToolButtonTextUnderIcon
# 	文本显示在图标下方
# Qt.ToolButtonFollowStyle
# 	遵循风格
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
tb.setAutoRaise(True)

menu = QMenu(tb)
# menu.setTitle("菜单")


sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("xxx.png"))

action1 = QAction(QIcon("xxx.png"), "行为1", menu)
action1.setData([1, 2, 3])
action2 = QAction("行为2", menu)
action2.setData({"name": "sz"})
# action.triggered.connect(lambda :print("点击了行为菜单选项"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

tb.clicked.connect(lambda :print("工具按钮被点击了"))

tb.setMenu(menu)
#
tb.setPopupMode(QToolButton.InstantPopup)

def do_action(action):
    print("点击了行为", action.data())
tb.triggered.connect(do_action)


# btn = QPushButton(window)
# btn.setText("一般按钮")
# btn.move(100, 100)
# btn.setFlat(True)
#
#
#
# btn.setMenu(menu)








# Qt.NoArrow
# 	无箭头
# Qt.UpArrow
# 	向上箭头
# Qt.DownArrow
# 	向下箭头
# Qt.LeftArrow
# 	向左箭头
# Qt.RightArrow
# 	向右箭头

tb.setArrowType(Qt.RightArrow)

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())