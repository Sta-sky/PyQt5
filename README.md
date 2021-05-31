## <u>PyQt5</u>总结

[TOC]



### 1、所有控件展示：

---



#### 1、按钮：

1.  *QPushButton*
2. *QCommandLinkButton* 
3. *QRidioButton*
4. *QCheckButton*

#### 2、输入控件：

##### 1、纯键盘输入：

1. *QLineEdit*
2. *QTextEdit*
3. *QPlainTextEdit*
4. *QKeySequenceEdit*

##### 2、步长调节 键盘 + 鼠标

1. *QDateTimeEdit*  ------- 时间采集	
   1. *QDateEdit*
   2. **QTimeEdit*
2. *QSpinBox*  ------  数字采集
3. *QDoubleSpinBox*   ----- 浮点型采集

##### 3、组合框输入：

1. QComboBox    ------ 组合框， 省份下城市选择可用
2. QFontComboBox ---  字体选择

##### 4、滑块：

1. QDial   ----- // 旋钮滑块
2. QSlider   ----------竖直滑条
3. QScrollBar ----------  滚动条

##### 5、对话框

1. QColorDialog   ---------- 颜色选择对话框
2. QFileDialog    ----------- 文件对话框
3. QFontDialog  -------------- 字体对话框
4.   QInpuutDialog  -----------   输入框

#### 3、日期

1. QCalendarWidget   ----   日期选择表格

#### 4、展示控件

1. QLabel
   1. 普通文本
   2. 数字
   3. 富文本
   4. 图片
   5. gif动画
2. QLCDNumber   -------------  LCD数字灯
3. QProgressBar   -------------  进度条
4. 对话框  =  --------------- 
   1.  QMessageBox  对话框
   2. QEooroMessage  --------- 错误对话框
   3. QProgressDialog  ------  进度条对话框

#### 5、容器控件

1. QToolBox  ---------   容器中可以添加按钮
2. QDoalogButtonBox  --------- 承载按钮
3. QGroupBox   ---------    承载组件  划分组
4. QMdisubWindow --------  窗口中创建子窗口



#### 6、结构控件

1. QMainWindow   
   1. QMenuBar  ------------  菜单栏
      1. QMenu
   2. QToolBar   ---------------  工具栏
      1. QToolButton
   3. QStatusBar   ----------- 底边框状态栏
2. QTabWidget   -------- 标签控件
   1.  QTabBar
3. QStackedWidget --------------  可以包含多个界面
4. QSplitter   -----------   分割界面
5. QDockWidget  --------  窗口中的组件可以移动

#### 7、滚动控件

1. QAbstractScrollArea   ---------   滚动控件
   1. QTextBrowser   --------------  文本浏览
   2. QScrollArea  --------------   滚动区域
   3. QAbstractltemView -------------  
      1. QColumnView  -------  列控件
      2. QHeaderView  --------  头部控件  eg：表头
      3. QListView
         1. QListWidget
         2. QUndoView
      4. QTableView
         1.  QTableWidget
      5. QTreeView
         1. QTreeWidget
   4. QMdiarea  ------------ 窗口中子窗口
   5. QGraphicsView  ------------- 绘图
   6.  QDesktopWdiget ------  电脑桌面信息 宽高之类的



#### 8、其他

1. QDialog  ----- 安装步骤
2. 打印 QAbstrastPrintDialog
3. 打印预览   QPrintPrevviewDialog
4. QPageSetupDialog   打印选项
5. 欢迎界面  QSplashScreen
6. QVideWidget ------- 视屏
7. QCameraWidget  ------- 相机控件
8. QWebEngineView   ----- 浏览器控件

---



### 2、事件机制

~~~~python
1、相比较于信号与槽机制，
	信号与槽机制是对事件机制的高级封装
    事件机制更偏向于底层	
    
2、事件的传递：
	1、如果一个控件没有处理发生的事件，则会自动传递给父控件进行处理。
	2、事件具备两个特殊方法：
    	event.accept()  ----- 接收该事件， 事件不再传递
        event.ignore()  ------ 忽略事件， 事件继续传递

3、那个控件接受键盘、或鼠标、或快捷键事件，使用：
	eg:
       label_img.grabKeyboard()
       label_img.grabMouse()
       label_img.shortcut()
~~~~

##### 1、显示和关闭事件

```python
showEvevt()
closeEvent()

```



##### 2、窗口移动事件

~~~python
moveEvent()  ----  窗口移动
~~~
##### 3、窗口尺寸改变事件

~~~python
resizeEvent()  ---- 窗口大小改变
~~~
##### 4、鼠标进入和离开事件

~~~python
enterEvent()   进入
leaveEvent()    离开
~~~
##### 5、鼠标按下，抬起，

~~~python
mousePressEvent()	鼠标按下
mouseReleaseEvent()	鼠标抬起
mouseDoubleClickEvent()	鼠标双击
mouseMoveEvent()	鼠标移动
~~~
##### 6、键盘按下抬起

~~~python
KeyPressEvent()  -----  键盘按下
KeyReleaseEvent()  ---- 键盘抬起

修饰键：
	键盘按下后不会输入任何东西
普通键：
	按下键盘会输入内容

event.modifiers() ------  获取修饰键位
event.key()   ----------  获取普通键位
eg：
	修饰键只有一个情况下
	if event.modifiers() == Qt.ControlModifier() and event.key():
        print("按下了 ctrl + s")
     修饰键有两个情况下
    if event.modifiers() == Qt.ControlModifier() |  Qt.ShiftModifier() and event.key():
        print("按下了 ctrl + shift + s")
~~~
##### 7、焦点事件

~~~~python
focusInEvent()  ----  获取焦点后
focusOutEvent()  ---- 失去焦点后
~~~~
##### 8、拖拽事件

~~~python
dragLeaveEvent() ---- -- 拖拽进入控件调用
dragLeaveEvent()  -------  拖拽离开控件调用
dragMoveEvent() --------- 拖拽在控件内移动时调用
dropEvent() ---------  拖拽释放时调用
~~~
##### 9、绘制事件

~~~python
paintEvent()   --------- 显示控件 或 更新控件调用
~~~
##### 10、改变事件

~~~python
changeEvent() ---------  窗体改变， 字体改变时调用
~~~
##### 11、右键 菜单

~~~python
contextMenuEvent()  ---------  访问右键菜单时调用
~~~
##### 12、输入法

~~~python
inputMethodEvent()   ----- 输入法调用
~~~





---



### 3、位置大小总结

~~~css
1、内容随窗口变化设置：
    1、设置自适应大小  ------  adjustSize()
    2、设置固定窗口 ---------  setFixedSize()
2、内容内边距设置
	设置： --- setContentMargins(left, up, right, bottom)
	获取： --- getContentMargins(left, up, right, bottom)
~~~

##### 1、根据点击位置，在父控件中，获取点击并设置背景

~~~python
eg：
	def mousePressEvent(self, event):
        sub_widget = self.childAt(event.x(), event.y())
        if sub_widget:
            sub_widget.setStyleSheet('backgound-color:red')
        else:
            pass      
~~~



##### 2、控件层级关系调整

```python
lower： 层级下沉
raise： 上升
```
##### 3、窗口状态

~~~python
windowStatus		获取状态
windowMaximized		最小化
windowMinimized		最大化
windownFullScreen  填满窗口
~~~
##### 4、窗口绘制

~~~python
1、显示隐藏控件：
    setVisible(bool)
    setHidden(bool)
    hide()
2、是否编辑状态：标题中添加[*] 
	setWindowModified
3、窗口激活 
	isActiveWindow
4、关闭控件
	程序运行中，隐藏并关闭控件后，释放资源
	setAttribute(Qt.WA_DeleteOnClose, True)
~~~
---



### 4、鼠标操作设置

~~~python
1、设置鼠标
	setCursor(Qt.BusyCursor) ------ ---繁忙
    setCursor(Qt.ForbiddenCursor) ---- 禁止
    setCursor(Qt.SplitVCursor) ---- 垂直
    setCursor(Qt.SplitHCursor) ---- 水平
    
    QCursor  ----  自定义鼠标图标
2、鼠标跟踪
	mouseMoveEvevt  ---------  鼠标跟踪事件
    
~~~



---

### 基础组件

#### 1、按钮 QAbstractButton

```python
1、所有按钮控件的基类
2、提供按钮的通用功能
 
3、按钮类信号：
	1、pressed()
    2、released()
    3、clicked()
    4、toggled()  ---- 状态切换
```

##### 1、QPushButton

```python
1、按钮类的自动重复：
	setAutoRepeat(bool)
    setAutoRepeatInterval(ms)  # 设置自动重复发送信号的间隔时间
    setAutoRepeatDelay(ms)  # 设置初次检测延迟时间  当按下多少秒后开始重复发送信号
    
2、按钮状态：
	1、isDown()
    	设置按钮为按下的状态 
        设置按钮按下的状态
        btn.setStyleSheet(QPushButton:pressed {background-color: red;})
    2、 isCheckable()
    	是否可以被选中
    3、isChecked()
    	判断是否选中了
    
3、按钮的排他性
	setAutoExclusive()  设置排他性
 
4、模拟信号：
	Click()		普通模拟点击,
	animateClick(ms)  动画模拟点击, 点击按钮带动效
    
5、按钮有效区域设置：
	重写： hitButton方法
    	eg： 点击按钮的右半部份才有效
    	def hitButton(self, point):
            # point 参照按钮的坐标
            print(point)
            if point.x() > sellf.width() / 2:
                return Trun
           	else:
                return False
6、特有功能：

	meun = QMenu() ----- 创建菜单
    meun.addAction('打开文件')  -----  添加行为
    meun.addSeparator  ------添加分割线
    btn.setMenu(menu)  ---  可以给按钮设置菜单；
    
7、扁平化
	setFlat()  设置扁平化， 颜色设置也随之失效

8、
	setAutoDefault()   --------- 点击之后设置为默认选中。
9、右键菜单
	添加右键菜单的两种方式：
    	1、重写右键菜单默认方法：
        class Windown(QWidget):
        	self.contentMenuEvent(self, event):
                # TODO 创建菜单
    	2、开启自定义菜单策略，默认菜单失效且不会
        	self.setContextMenuPolicy(Qt.CustomContextMenu)  -- 打开策略
            self.customContextMenuRequested.connect(self.create_menu) --- 菜单信号连接 
        	 
```



