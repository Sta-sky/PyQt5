import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication


class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QtCore.QRect(100,100, 1500, 900 ))
        layout = QtWidgets.QVBoxLayout(self)
        self.clipboardLabel = QtWidgets.QLabel()
        layout.addWidget(self.clipboardLabel)
        self.tableWidget = QtWidgets.QTableWidget(10, 10)
        layout.addWidget(self.tableWidget)
        self.tableWidget.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.tableWidget.indexAt(event.pos())
                if index.data():
                    self.clipboardLabel.setText(index.data())
            elif event.button() == QtCore.Qt.RightButton:
                index = self.tableWidget.indexAt(event.pos())
                if index.isValid():
                    item = self.tableWidget.itemFromIndex(index)
                    if not item:
                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(index.row(), index.column(), item)
                    item.setText(self.clipboardLabel.text())
        return super().eventFilter(source, event)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    exec(app.exec_())