# -*- coding: utf-8 -*-
import sys
import psycopg2
import time, datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from tables import Ui_dataBaseForm


class MyMain(QMainWindow, Ui_dataBaseForm):
    # conn = psycopg2.connect(database="postgres", user="postgres", password="0818", host="localhost", port="5432")
    # cursor = conn.cursor()

    def __init__(self):
        super().__init__()
        self.setupUi(self)  ## 初始化运行A窗口类下的 setupUi  函数
    #     self.db_create.clicked.connect(self.createBase)  # 创建数据库表
    #     self.db_delete.clicked.connect(self.deleteBase)  # 删除表格
    #     self.db_insert.clicked.connect(self.dbWrit)  # 插入数据
    #     self.db_delete_row.clicked.connect(self.deleteRow)  # 删除行
    #     self.date_select.clicked.connect(self.dateSelect)  # 查询输出
    #     self.db_export.clicked.connect(self.excelExport)  # 导出CSV
    #
    # # 报警提示框
    # def alarmMessageBox(self, alarm):
    #     self.alarm = alarm
    #     reply = QMessageBox.information(self, "提示框", self.alarm, QMessageBox.Yes,
    #                                     QMessageBox.Yes)

    # 创建表格
    # def createBase(self):
    #     try:
    #         self.dbName = self.db_create_edit.text()  # 设置表名
    #         MyMain.cursor.execute("CREATE TABLE %s (    \
    #          date  timestamp without time zone NOT NULL, \
    #          id  serial  NOT NULL,  \
    #          line1 CHAR(6) NOT NULL,\
    #          line2 CHAR(6) NOT NULL,\
    #          line3 CHAR(6) NOT NULL,\
    #          PRIMARY KEY (date));" % (self.dbName))  ## 创建表SQL命令
    #         MyMain.conn.commit()
    #         self.alarmMessageBox("创建表格成功！")
    #     except Exception as exc:
    #         self.alarmMessageBox(str(exc))
    #         触发报警框
    #         MyMain.conn.commit()  ## 给数据库，开启新的事物块。
    #
    # # 删除表格
    # def deleteBase(self):
    #     try:
    #         self.dbName = self.db_delete_edit.text()  # 设置表名
    #         MyMain.cursor.execute("DROP TABLE %s " % (self.dbName))  ## 创建execu test 数据库SQL命令
    #         MyMain.conn.commit()
    #         self.alarmMessageBox("删除表格完成！")
    #     except Exception as exc:
    #         self.alarmMessageBox(str(exc))
    #         MyMain.conn.commit()
    #
    #         # 写入数据
    #
    # def dbWrit(self):
    #     self.dbName = self.db_create_edit.text()
    #     self.text = self.db_writ.text().split()  # 读取界面框数据
    #     # print(self.text)
    #     print(len(self.text))
    #     if len(self.text) != 3:
    #         self.alarmMessageBox("数据为 %d 个，不符合要求。" % (len(self.text)))
    #     else:
    #         try:
    #             MyMain.cursor.execute(
    #                 "INSERT INTO {0} (date,line1,line2,line3) VALUES((SELECT now()),'{1}', '{2}' , '{3}')"
    #                     .format(self.dbName, self.text[0], self.text[1], self.text[2]))
    #             MyMain.conn.commit()
    #         except Exception as exc:
    #             self.alarmMessageBox(str(exc))
    #             MyMain.conn.commit()
    #             # 删除最后一行
    #
    # def deleteRow(self):
    #     self.dbName = self.db_create_edit.text()
    #     try:
    #         MyMain.cursor.execute("DELETE FROM {0} WHERE date= (SELECT max(date)  FROM {0})".format(self.dbName))
    #         MyMain.conn.commit()
    #         self.alarmMessageBox("删除最后一行成功！")
    #     except Exception as exc:
    #         self.alarmMessageBox(str(exc))
    #         MyMain.conn.commit()
    #
    # # 查询的条件
    # def rogatoryCondition(self):
    #     self.startTime = self.date_start.dateTime().toString("yyyy-MM-dd hh:mm:ss")
    #     self.endTime = self.date_end.dateTime().toString("yyyy-MM-dd hh:mm:ss")
    #
    #     self.dbName = self.db_create_edit.text()
    #     self.select = "SELECT date, id ,line1,line2,line3 FROM {0} WHERE date > '{1}' and  date < '{2}'".format(
    #         self.dbName,
    #         self.startTime,
    #         self.endTime)
    #     return self.select
    #
    # # 查询输出
    # def dateSelect(self):
    #     self.condition = self.rogatoryCondition()
    #     try:
    #         MyMain.cursor.execute(self.condition)
    #         self.data = MyMain.cursor.fetchall()
    #         self.rowNum = len(self.data)  # 获取查询到的行数
    #         self.columnNum = len(self.data[0])  # 获取查询到的列数
    #
    #         self.dataView.setRowCount(self.rowNum)  # 设置表格行数
    #         self.dataView.setColumnCount(self.columnNum)
    #
    #         for i, da in enumerate(self.data):
    #             for j in range(self.columnNum):
    #                 self.itemContent = QTableWidgetItem(('%s') % (da[j]))
    #                 self.dataView.setItem(i, j, self.itemContent)
    #         self.alarmMessageBox("查询完成！")
    #     except Exception as exc:
    #         self.alarmMessageBox(str(exc))
    #         MyMain.conn.commit()
    #
    # def excelExport(self):
    #     self.condition = self.rogatoryCondition()
    #     MyMain.cursor.execute("COPY( {0} ) TO 'D:/ExceptionData.csv' with csv header".format(self.condition))
    #     self.alarmMessageBox("导出成功！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    A1 = MyMain()
    A1.show()
    sys.exit(app.exec_())
