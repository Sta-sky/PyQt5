from PyQt5.Qt import *

# print(QObject.__subclasses__())
# print(QWidget.__subclasses__())
# print(QAbstractButton.__subclasses__())


def getSubClasses(cls):

    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__()) > 0:
            getSubClasses(subcls)

getSubClasses(QAbstractButton)