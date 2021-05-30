# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def contextMenuEvent(self, evt):
        print("默认上下文菜单调用这个方法")
        menu = QMenu(self)

        # 子菜单 最近打开

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")
        # open_recent_menu.setIcon()

        # 行为动作 新建  打开  分割线 退出
        # new_action = QAction()
        # new_action.setText("新建")
        # new_action.setIcon(QIcon("xxx.png"))
        new_action = QAction(QIcon("xxx.png"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建文件"))

        open_action = QAction(QIcon("xxx.png"), "打开", menu)
        open_action.triggered.connect(lambda: print("打开文件"))

        exit_action = QAction("退出", menu)
        exit_action.triggered.connect(lambda: print("退出程序"))

        file_action = QAction("Python-GUI编程-PyQt5")

        menu.addAction(new_action)
        menu.addAction(open_action)
        open_recent_menu.addAction(file_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()
        menu.addAction(exit_action)

        # point
        menu.exec_(evt.globalPos())
        # menu.exec_(evt.pos())

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("按钮的功能")
window.resize(500, 500)


btn = QPushButton(window)
btn.setParent(window)
btn.setText("xxx")
btn.setIcon(QIcon("xxx.png"))


# *************菜单的设置***************开始
menu = QMenu(window)

# 子菜单 最近打开

open_recent_menu = QMenu(menu)
open_recent_menu.setTitle("最近打开")
# open_recent_menu.setIcon()


# 行为动作 新建  打开  分割线 退出
# new_action = QAction()
# new_action.setText("新建")
# new_action.setIcon(QIcon("xxx.png"))
new_action = QAction(QIcon("xxx.png"), "新建", menu)
new_action.triggered.connect(lambda :print("新建文件"))

open_action = QAction(QIcon("xxx.png"), "打开", menu)
open_action.triggered.connect(lambda :print("打开文件"))

exit_action = QAction("退出", menu)
exit_action.triggered.connect(lambda :print("退出程序"))

file_action = QAction("Python-GUI编程-PyQt5")


menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(exit_action)





# btn.setMenu(menu)

# print(btn.menu())

# btn.setStyleSheet("background-color: red;")
# btn.setFlat(True)
# print(btn.isFlat())



# *************菜单的设置***************结束

btn2 = QPushButton(window)
btn2.setText("btn2")
btn2.move(200, 200)

btn2.setAutoDefault(True)

print(btn.autoDefault())
print(btn2.autoDefault())

btn2.setDefault(True)


def show_menu(point):
    menu = QMenu(window)

    # 子菜单 最近打开

    open_recent_menu = QMenu(menu)
    open_recent_menu.setTitle("最近打开")
    # open_recent_menu.setIcon()

    # 行为动作 新建  打开  分割线 退出
    # new_action = QAction()
    # new_action.setText("新建")
    # new_action.setIcon(QIcon("xxx.png"))
    new_action = QAction(QIcon("xxx.png"), "新建", menu)
    new_action.triggered.connect(lambda: print("新建文件"))

    open_action = QAction(QIcon("xxx.png"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))

    exit_action = QAction("退出", menu)
    exit_action.triggered.connect(lambda: print("退出程序"))

    file_action = QAction("Python-GUI编程-PyQt5")

    menu.addAction(new_action)
    menu.addAction(open_action)
    open_recent_menu.addAction(file_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()
    menu.addAction(exit_action)

    # point
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)

window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)

# btn.show()


# 2.3 展示控件
window.show()

# btn.showMenu()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())