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

##### 2、定时器

~~~python
qtime = QTime（）
def test_time():
	pass
qtime.timeout.connect(test_time)


~~~

##### 3、进度管理QProgressDialog

~~~python
1、创建与使用:
    pd = QProgressDialog(str_1, str_2, int_1, int_2)
	参数解释:
    	str_1: 描述信息，
        str_2: 取消按钮文本
        int_1 : 最小值
        int_2: 最大值
    
2、显示
   手动打开:
        pd.show()  --- 非模态
        pd.open()   ----  模态 -- 只能操作当前窗口
        
  	设置打开时间：
    	pd.setMinimumDuration(ms)
        
   手动设置模态：
    	pd.setModal(True)
        
        
   自动重置、关闭:
    	pd.setAutoReset()
        pd.setAutoClose()
        
   关闭取消按钮
        self.progress.setCancelButtonText(None)

    
3、设置
	获取:
        最大值 maximum
        最小值 minimum
        当前进度百分比: value
    设置:
        最大值  setMIniximum(int)
        最小值  setMaximum(int)
        区间: setRange(int, int)
	

~~~



---



### 布局管理器

~~~python
QHLayoutBox()

1、设置布局对象参数
	1、设置布局管理器外边距
    	hor.setContensMargins(self, nit, int, int, int)
    2、设置管理器中组件之间的间距
    	hor.setSpacing(self, int)
2、调整布局方向：
	布局从右向左
	hor.setLayoutDirection(Qt.RightToLeft)
  
~~~



##### 1、QLayout、

~~~python
基类

1、添加控件
    layout.addwidget(self.label_1)

2、替换控件
    layout.replaceWidget(self.label_1, self.label_2)
    self.label_1.hide()

~~~

##### 2、QBoxLayout ，QHBoxLayout, QVBoxLayout盒子布局

~~~python
水平布局

1、修改方向：
	hor_setDirection(QBoxLayout.verBoxLayout)
2、添加子控件：
	在控件1的位置插入label标签
	layout.insertWidget(1, label)
3、移出标签
	1、删除
        layout.removewidget(label)
        lable.setParent(None)    ------后续无用的情况下删除
	2、隐藏
    	label.hide()  ------- 再次会调用的情况下使用
4、添加空白
				-----------调整盒子内组件label_1, label_2的间距为100
	layout.addwidget(label_1)
	layout.addSpacing()
    layout.addwidget(laebl_2)
5、插入空白：
	在1、2组件之间插入100的空白
	insertSpaing(1, 100)
6、伸缩因子：
	eg:
        在布局管理器中
        	label_1占据3/1， laebl_2占据2/3
    layout.addwidget(label_1, stretch=1 )
   	layout.addwidget(label_2, stretch=2 )
7、添加空白的伸缩因子
	eg:
        在label_1、label_2之间添加空白因子：
        	总共分为 5 份， 空白占2份
    layout.addwidget(label_1, stretch=1 )
    layout.addStretch(2) 
   	layout.addwidget(label_2, stretch=2 )
 8、给子控件，或子布局添加伸缩因子：
	子布局
	layout.setStrechFacto(label_1, 1)
    子布局
    layout.setStrechFactor(hor_box, 2)

    
~~~

##### 2、QFormLayout  表单布局

~~~python
作用：
	管理标签，输入框控件；
    用于 提示信息， 输入文本，例如登录注册界面的输入提示框
    结构为 两列多行：
    	---  +++++
        ---  +++++
        ---  +++++
        ---  +++++
        ---  +++++
    
1、表单管理器的  添加行
	additem()  ----------- 添加为上下结构  两行
	addRow()  --------  添加为左右结构  一行
    	addRow(Qwidget, Qwidget) ----   添加 两个组件  成为一行
        addRow(Qwidget, QLayout) -----  添加组件 跟布局 成为一行
        addRow(str, Qwidget) ---------  添加字符串，跟组件 成为一行
        addRow(str, QLaytou) - ------   添加 字符串，跟布局，成为一行
        addRow(self, Qwidget) --------  添加一个控件 为一行
        addRow(self, QLayout)  -------  添加一个盒子布局 为一行
	eg:
        为每行添加 label提示信息， 和文本输入框 text_1， 组成登陆界面
	layout = QFormLayout()
    layout.addRow(label_1, text_1)
    layout.addRow(label_2, text_2)
    layout.addRow(label_3, text_3)

2、表单管理器的  插入行：
	int: 索引
	addRow(int, Qwidget, Qwidget)
    
3、获取行结果:
    
    # 获取总行数：
        count = layout.getRow()
    # 获取组件位置：
        tupel_result = layout.getWidgetPosition(self, label_1)
        
    # 获取 单行是一个布局管理器，
    tuple_result = layout.getlayoutPosition(self, QLayout)
    
4、修改行
	int:   指明索引
    QFramLayout.ItemRole： 修改的角色是，行中第一个还是第二个
        LabelRole   ---  第一个  角色
        FieldRole   ---  第二个  角色

    添加布局：
        layout.setLaytou(self, int, QFramLayout.ItemRole, QLayout)
	
    添加控件:
        layout.setWidget(self, int, QFramLayout.ItemRole, QWidget)
~~~



##### 3、网格布局 QGildLayout

~~~python
layout = QGildLayout()

1、创建并添加：
	layout.addWidget(label, row_int, col_int，align_row, align_col)
    layout.addLayout(label, row_int, col_int，align_row, align_col)
        row_int: 行索引
        col_int:列索引
        alignment: 跨度， --- 占据了几列
            eg： label在第 1行， 第1列 占据了 2行， 3列
                layout.addWidget(label, 1, 1， 2, 3)
	eg:  第一行添加了 3 个标签
        layout.addWidget(label_1, 0, 0)
        layout.addWidget(label_2, 0, 1)
        layout.addWidget(label_3, 0, 2)

~~~



##### 4、堆叠布局 QStackedLayout

~~~python
1、创建并添加:
    
    layout = QStackedLayout(self)
    
    layout.addwidget(laebl_1)
    layout.addwidget(laebl_2)
    layout.addwidget(laebl_3)
    
2、插入控件或布局
	layout.insertwidget(index_int, label)

3、页面切换:
        # 获取子控件的个数
        count = layout.count()
    1、根据索引值来设置:
        1、获取索引值
        	index = layout.currentIndex()
        2、设置
            layout.setCurrnetIndex(index)
           
   2、根据当前组件来设置
		1、获取组件
    		widget = layout.currentWidget()
       	 2、设置
			setCurrentWidget(self, widget)
4、信号：
	currentChange(int_index) ----  当前组件发生变化 传输信号  
    widgetRomoved(int_index)  ---- 当前组件被移除后  传输信号
~~~













































































