# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QLineEdit功能测试")
window.resize(500, 500)

le_a = QLineEdit(window)
le_a.move(100, 200)

le_b = QLineEdit(window)
le_b.move(100, 300)

# le_b.setEchoMode(QLineEdit.PasswordEchoOnEdit)
# print(le_b.echoMode())

copy_btn = QPushButton(window)
copy_btn.setText("复制")
copy_btn.move(100, 400)

def copy_cao():
    # 1. 获取文本框a, 内容
    # content = le_a.text()
    # # 2. 把上面获取到的内容, 设置到文本框B里面
    # # le_b.setText(content)
    # # le_b.setText("")
    # # le_b.insert(content)
    # print(le_b.text())
    # print(le_b.displayText())
    print(le_b.isModified())
    le_b.setModified(False)

copy_btn.clicked.connect(copy_cao)


# 最大长度限制
le_a.setMaxLength(3)
print(le_a.maxLength())

le_a.setReadOnly(True)

le_a.setText("王炸, 要不起!")

# le_b 设置掩码
# 总共输入5 位  左边 2(必须是大写字母) - 右边 2(必须是一个数字)
# le_b.setInputMask(">AA-99;#")
# le_b.setInputMask("9999-9999999;0")





# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())