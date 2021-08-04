import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from logic.MainWindown import EmailWindown

if __name__ == '__main__':
	email_app = QApplication(sys.argv)
	window = EmailWindown()
	window.show()
	sys.exit(email_app.exec_())
	




