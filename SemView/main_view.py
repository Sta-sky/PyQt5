import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication

from SemView.main_logic import MainWindown



if __name__ == '__main__':
    app = QApplication(sys.argv)
    objs = MainWindown()
    objs.show()
    app.exec_()

