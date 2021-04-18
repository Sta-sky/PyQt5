from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from SemView.data import table_data
from util.tools import handle_img
from SemView.main_ui import MyMainView


class MainWindown(MyMainView):
    def __init__(self):
        super(MainWindown, self).__init__()
		
        # 表格点击事件
        self.table_view.cellClicked.connect(self.handle_signal)
        
        # 初始化 text 框中信息
        self.text_edit.setText("请点击表格查看详细数据")
        
        # 表格类型展示 选择 点击事件
        self.table_btn1.clicked.connect(self.table_btn1_Clicked)
        self.table_btn2.clicked.connect(self.table_btn2_Clicked)
        
        # 文本框点击事件
        self.tab_sort_click1.clicked.connect(self.desc_sort_click)
        self.tab_sort_click2.clicked.connect(self.asc_sort_click)
        self.tab_sort_click3.clicked.connect(self.recover_sort_data)


    def handle_signal(self, row, col):
        print(row, col)
        info = None
        try:
            content = self.table_view.item(row, col).text()
            info = f"""<font color='red' size='10'><red>行信息为 {str(row)}, <br>
                        行信息为 {str(col)} <br>内容为 {str(content)}</font>"""
            if row == 1 and col == 1:
                img_obj = handle_img(self, '../util/test1.png')
                self.label_view.setPixmap(QPixmap(img_obj))
            elif row == 1 and col == 2:
                img_obj = handle_img(self, '../util/test3.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
            elif row == 1 and col == 3:
                img_obj = handle_img(self, '../util/test2.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
            else:
                img_obj = handle_img(self, '../util/test4.jpg')
                self.label_view.setPixmap(QPixmap(img_obj))
        except Exception as e:
            info = f"""<font color='red' size='3'><red>行信息为 {str(row)},
                        \n行信息为 {str(col)} \n    内容为 None </font>"""
            self.label_view.setText("当前数据无图片可显示")
        finally:
            self.text_edit.setHtml(info)

    def table_btn1_Clicked(self):
        # TODO Table View 表格类型展示
        self.label_view.setPixmap(QPixmap(handle_img(self, '../util/test.jpg')))

    def table_btn2_Clicked(self):
        # TODO Wafer View 表格类型展示
        self.label_view.setPixmap(QPixmap(handle_img(self, '../util/test1.png')))

    def desc_sort_click(self):
        try:
            col_num = self.table_view.currentColumn()
            print(f'当前行数{col_num}')
            self.table_view.sortItems(int(col_num),Qt.DescendingOrder)  # 设置第几行排序
            self.table_view.setSortingEnabled(True)  # 设置表头可以自动排序
        except Exception as e:
            print(e)
            raise

    def asc_sort_click(self):
        try:
            col_num = self.table_view.currentColumn()
            print(f'当前行数{col_num}')
            self.table_view.sortItems(int(col_num),Qt.AscendingOrder)  # 设置第几行排序
            self.table_view.setSortingEnabled(False)  # 设置表头可以自动排序
        except Exception as e:
            print(e)
            raise

    def recover_sort_data(self):
            table_data(self.table_view)

    def get_current_row(self):
        row_num = self.table_view.currentRow()
        
