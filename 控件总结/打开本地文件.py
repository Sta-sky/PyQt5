# QFileDialog
#           文件选择对话框
#                       允许用户选择文件，
#                       遍历文件系统，以选择一个或者多个文件目录

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFileDialog_文件选择')
        self.resize(500,500)
        self.fd = QFileDialog(self,'葵花宝典','../','所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        # self.fd.show()
        self.iniUI()


    def iniUI(self):
        # self.getOpenFileName_()
        # self.getOpenFileNames_()
        # self.getOpenFileUrl_()
        # self.getOpenFileUrls_()
        # self.getSaveFileName_()
        # self.getSaveFileUrl_()
        # self.getExistingDirectory_()
        # self.getExistingDirectoryUrl_()
        # self.constructFunc()
        # self.setAcceptMode_()
        # self.setFileMode_()
        # self.setNameFilter_()
        self.fileDialogEvent()

    ##############################################使用静态方法，快捷获取文件路径
    #
    # 现在需求:
    #           使用静态方法，快捷获取文件路径
    #          ( 父控件 ， '对话框标题', '文件路径' , ' 过滤器名称1(*.后缀名1 *.后缀名2 g);;过滤器名称2(*.后缀名1 *.后缀名2 ) ')
    # 解决方法:
    #           QFileDialog.getOpenFileName()
    #           QFileDialog.getOpenFileNames()
    #           QFileDialog.getOpenFileUrl()
    #           QFileDialog.getOpenFileUrls()
    #           QFileDialog.getSaveFileName()
    #           QFileDialog.getSaveFileUrl()
    #           QFileDialog.getExistingDirectory()
    #           QFileDialog.getExistingDirectoryUrl()
    def getOpenFileName_(self):
        result1 = QFileDialog.getOpenFileName(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        # result1 是一个元组，元组元素均为字符串，
        # 第一个元素是 所打开的文件 绝对路径，
        # 第二个元素是 所选择的过滤器字符串
        print(result1)

    def getOpenFileNames_(self):
        result2 = QFileDialog.getOpenFileNames(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        # result2 是一个元组，元组元素均为字符串，
        # 第一个元素是 所打开的多个文件 绝对路径 组成的列表，列表每个元素均为文件绝对路径字符串，
        # 第二个元素是 所选择的过滤器字符串
        print(result2)

    def getOpenFileUrl_(self):
        result3 = QFileDialog.getOpenFileUrl(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        print(result3)  # 第一个元素 是一个包含文件绝对路径字符串的 QUrl对象，不是字符串类型了

    def getOpenFileUrls_(self):
        result4 = QFileDialog.getOpenFileUrls(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        print(result4)

    def getSaveFileName_(self):
        result5 = QFileDialog.getSaveFileName(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        print(result5)

    def getSaveFileUrl_(self):
        result6 = QFileDialog.getSaveFileUrl(self, '葵花宝典', './', '所有文件(*.*);;Python文件(*.py);;图片(*.png *.jpg)')
        print(result6)

    def getExistingDirectory_(self):
        result7 = QFileDialog.getExistingDirectory(self, '葵花宝典', './')  # 不需要过滤器

        print(type(result7), result7)  ## result7 只是一个文件夹的绝对路径,！！！不带引号的纯字符串

    def getExistingDirectoryUrl_(self):
        result8 = QFileDialog.getExistingDirectoryUrl(self, '葵花宝典', QUrl('./'))  # 不需要过滤器
        print(result8)  # PyQt5.QtCore.QUrl('file:///E:/Python/code/GUI')  返回一个QUrl()对象

    ##############################################################################使用静态方法，快捷获取文件路径


    ##############################################文件对话框 构造函数
    #
    #
    #
    def constructFunc(self):
        self.fd.fileSelected.connect(lambda str_:print('选择了文件:',str_))#文件对话框文件被选择时发射的信号
    #############################文件对话框 构造函数

    ##############################################文件对话框 打开或者保存 接受模式设置
    #
    #设置
    #
    def setAcceptMode_(self):
        # self.fd.setAcceptMode(QFileDialog.AcceptOpen)
        self.fd.setAcceptMode(QFileDialog.AcceptSave)
        self.fd.fileSelected.connect(lambda str_:print('选择了文件:',str_))
        self.fd.setDefaultSuffix('txt')#设置默认的后缀名
    #############################文件对话框 打开或者保存 接受模式设置


    ##############################################文件对话框 文件模式设置 类似于文件过滤
    #
    # 类似于文件过滤，
    #           设置文件是 单选模式 或者 多选模式
    #
    #
    #
    def setFileMode_(self):
        # self.fd.setFileMode(QFileDialog.ExistingFile) #单个现有文件
        # self.fd.setFileMode(QFileDialog.ExistingFiles) #可以多选文件，多个现有文件
        # self.fd.setFileMode(QFileDialog.Directory)    #只能选择目录
        self.fd.setFileMode(QFileDialog.AnyFile)        #任何文件，无论是否存在

        self.fd.fileSelected.connect(lambda str_:print('选择了文件:',str_))
    #############################文件对话框 文件模式设置 类似于文件过滤


    ##############################################文件对话框文件名称 字符串过滤器
    #
    # 针对文件名称 进行过滤
    #
    def setNameFilter_(self):
        self.fd.setNameFilters( ['所有文件(*.*)','图片(*.png *.jpg)','Python文件(*.py)'] )
    #############################文件对话框 文件名称 字符串过滤器

    ##############################################文件对话框 信号相关
    #
    # 现在需求:
    #           文件对话框 信号相关
    #
    # 解决方法:
    #           fd.currentChanged.connect( lambda path_str:)
    #           fd.currentUrlChanged.connect(lambda QUrl():)
    #           fd.directoryEntered.connect(lambda directory_str:)
    #           fd.filterSelected.connect(lambda filter_str:)
    #           fd.fileSelected.connect(lambda file_path_str:)
    #           fd.filesSelected.connect(lambda [file_path_str]:)
    #
    #
    def fileDialogEvent(self):
        ### 返回 点击到的任意文件或文件夹 的绝对路径 (真的只是点击到，不需要双击进入的)
        # self.fd.currentChanged.connect(lambda path_str:print(path_str))

        ### 当鼠标双击进入某个文件夹时，返回 文件夹的完整路径
        self.fd.directoryEntered.connect(lambda directory_str:print('进入文件夹',directory_str))

        ### 当鼠标选择不同的文件过滤器时，返回所选择的过滤器名称
        self.fd.filterSelected.connect(lambda filter_str:print('过滤器',filter_str))

        ###当选中的单个文件时，多文件被选中 filesSelected的信号也会被发射
        ###但是选中多个文件时，只有多文件被选中，filesSelected的信号会被发射
        self.fd.setFileMode(QFileDialog.ExistingFiles)#设置为可多选模式
        self.fd.fileSelected.connect(lambda file_path_str:print('单个文件被选中',file_path_str))
        self.fd.filesSelected.connect(lambda Iter:print('多个文件被选中',Iter))
    #############################文件对话框 信号相关


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
