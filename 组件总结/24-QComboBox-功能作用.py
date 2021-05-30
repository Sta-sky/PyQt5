from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        cb.addItems(["abc", "123", "456"])
        cb.addItem(QIcon("xxx.png"), "撩课", {"name": "itlike"})

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cb.count()))
        # btn.clicked.connect(lambda :print(cb.currentIndex()))
        # btn.clicked.connect(lambda :print(cb.currentText()))
        # btn.clicked.connect(lambda :print(cb.currentData()))
        # btn.clicked.connect(lambda : btn.setIcon(cb.itemIcon(cb.currentIndex())))
        # btn.clicked.connect(lambda _, idx = cb.count()-1:print(cb.itemIcon(idx), cb.itemText(idx), cb.itemData(idx)))
        # btn.clicked.connect(lambda :cb.addItem("it"))
        # btn.clicked.connect(lambda :cb.clear())
        # btn.clicked.connect(lambda :cb.clearEditText())
        # btn.clicked.connect(lambda :cb.showPopup())
        btn.clicked.connect(lambda :cb.setCurrentIndex(2))
        cb.setMaxCount(6)
        cb.setEditable(True)
        # cb.setMaxVisibleItems(3)
        # cb.setDuplicatesEnabled(True)
        cb.setDuplicatesEnabled(True)


        cb.setCompleter(QCompleter(["123", "abc", "aaa", "bbb"]))

        # cb.activated[str].connect(lambda val:print("条目被激活", val))

        # cb.currentIndexChanged[str].connect(lambda val:print("当前索引发生改变", val))
        # cb.currentTextChanged.connect(lambda val:print("当前文本发生改变", val))
        # cb.editTextChanged.connect(lambda val:print("当前编辑文本发生改变", val))
        # cb.highlighted[int].connect(lambda val:print("高亮发生改变", val))
        cb.highlighted[str].connect(lambda val:print("高亮发生改变", val))




        # cb.setFrame(False)

        # cb.setIconSize(QSize(60, 60))
        # cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)




        # cb.addItem("xx1")
        # cb.addItem("xx2")
        # cb.addItem(QIcon("xxx.png"), "xx3")
        # cb.addItems(["1", "2", "3"])
        # cb.addItems(("1", "2", "3"))
        # cb.addItems("123")
        # cb.insertItem(1, "xxx")
        # cb.insertItem(1, QIcon("xxx.png"), "xxx")
        # cb.insertItems(1, ("1", "a", "b"))

        # cb.setItemIcon(2, QIcon("xxx.png"))
        # cb.setItemText(2, "社会顺")
        # # cb.removeItem(2)
        # cb.insertSeparator(2)
        #
        # # cb.setCurrentIndex(1)
        # cb.setCurrentText("社会顺")

        # cb.setEditable(True)
        # cb.setEditText("itlike")
        # cb.resize(400, 30)
        # print(QAbstractItemModel.__subclasses__())
        # model = QStandardItemModel()
        #
        # item1 = QStandardItem("item1")
        # item2 = QStandardItem("item2")
        # item22 = QStandardItem("item22")
        # item2.appendRow(item22)
        # model.appendRow(item1)
        # model.appendRow(item2)
        # cb.setModel(model)
        #
        # cb.setView(QTreeView(cb))




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())