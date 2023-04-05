import sys
import numpy as np
import scipy.spatial as spatial
from PyQt5 import uic
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()
        self.stc = None
        self.flag = 0

    def init_ui(self):
        with open('LInecharts_code.ui', 'r', encoding='utf-8') as f:
            self.ui = uic.loadUi(f, self)
        self.ui.setFixedSize(1044, 670)  # 设置初始大小

        # 将groupBox的边框设置为无色
        self.ui.groupBox.setStyleSheet("QGroupBox {border:none}")
        self.ui.groupBox_2.setStyleSheet("QGroupBox {border:none}")

        self.frame = self.ui.frame
        self.textbrowser = self.ui.textBrowser
        self.tx1_select = self.ui.radioButton
        self.tx2_select = self.ui.radioButton_2
        self.name_text = 'TX1'

        self.DDM_button = self.ui.pushButton_6
        self.SDM_button = self.ui.pushButton_7
        self.RF_button = self.ui.pushButton_8
        self.num = self.ui.lineEdit_2
        self.label = self.ui.label_2
        validator = QIntValidator(1,100, self)
        self.num.setValidator(validator)

        self.modselect = self.ui.checkBox
        self.modselect.stateChanged.connect(self.checkboxChanged)

        self.LOC_CL = self.ui.pushButton
        self.LOC_DS = self.ui.pushButton_2
        self.LOC_NF = self.ui.pushButton_3
        self.LOC_CLR = self.ui.pushButton_4

        self.GP_CL = self.ui.pushButton_12
        self.GP_DS = self.ui.pushButton_10
        self.GP_NF = self.ui.pushButton_13
        self.GP_CLR = self.ui.pushButton_11

        self.tx1_select = self.ui.radioButton  # 设备选择按钮
        self.tx2_select = self.ui.radioButton_2
        self.tx1_select.clicked.connect(self.tx_select1)
        self.tx2_select.clicked.connect(self.tx_select2)

        # 为每个按钮添加一个点击事件处理函数
        self.LOC_CL.clicked.connect(self.handle_LOC_CL_click)
        self.LOC_DS.clicked.connect(self.handle_LOC_DS_click)
        self.LOC_NF.clicked.connect(self.handle_LOC_NF_click)
        self.LOC_CLR.clicked.connect(self.handle_LOC_CLR_click)
        self.GP_CL.clicked.connect(self.handle_GP_CL_click)
        self.GP_DS.clicked.connect(self.handle_GP_DS_click)
        self.GP_NF.clicked.connect(self.handle_GP_NF_click)
        self.GP_CLR.clicked.connect(self.handle_GP_CLR_click)

        # 设置按钮点击后变色
        self.LOC_CL.clicked.connect(self.color1)
        self.LOC_DS.clicked.connect(self.color2)
        self.LOC_NF.clicked.connect(self.color3)
        self.LOC_CLR.clicked.connect(self.color4)
        self.GP_CL.clicked.connect(self.color5)
        self.GP_DS.clicked.connect(self.color6)
        self.GP_NF.clicked.connect(self.color7)
        self.GP_CLR.clicked.connect(self.color8)

        self.helpbutton = self.ui.pushButton_9
        self.helpbutton.clicked.connect(self.framehide)
        self.stc = 0

        # 选择LOC或GP相关按钮隐藏设置
        self.locselect = self.ui.radioButton_3
        self.gpselect = self.ui.radioButton_4
        self.locselect.clicked.connect(self.LOC_hide)
        self.gpselect.clicked.connect(self.GP_hide)

        # 设置“存储设置”下相关部件
        self.data_address = self.ui.lineEdit
        self.button_save_address = self.ui.pushButton_5
        self.button_save_address.clicked.connect(self.save_address)

    def checkboxChanged(self, state):
        if state == 2:  # Qt.Checked
            self.flag = 1
            return self.flag
        else:
            self.flag = 0
            return self.flag

    def pushbutton_color(self):
        self.DDM_button.clicked.connect(self.color9)
        self.SDM_button.clicked.connect(self.color10)
        self.RF_button.clicked.connect(self.color11)

    def color1(self):
        self.LOC_CL.setStyleSheet("background-color: rgb(169,169,169)")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color2(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("background-color: rgb(169,169,169)")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color3(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("background-color: rgb(169,169,169)")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color4(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("background-color: rgb(169,169,169)")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color5(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("background-color: rgb(169,169,169)")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color6(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("background-color: rgb(169,169,169)")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("")

    def color7(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("background-color: rgb(169,169,169)")
        self.GP_CLR.setStyleSheet("")

    def color8(self):
        self.LOC_CL.setStyleSheet("")
        self.LOC_DS.setStyleSheet("")
        self.LOC_NF.setStyleSheet("")
        self.LOC_CLR.setStyleSheet("")
        self.GP_CL.setStyleSheet("")
        self.GP_DS.setStyleSheet("")
        self.GP_NF.setStyleSheet("")
        self.GP_CLR.setStyleSheet("background-color: rgb(169,169,169)")

    def color9(self):
        self.DDM_button.setStyleSheet("background-color: rgb(169,169,169)")
        self.SDM_button.setStyleSheet("")
        self.RF_button.setStyleSheet("")

    def color10(self):
        self.DDM_button.setStyleSheet("")
        self.SDM_button.setStyleSheet("background-color: rgb(169,169,169)")
        self.RF_button.setStyleSheet("")

    def color11(self):
        self.DDM_button.setStyleSheet("")
        self.SDM_button.setStyleSheet("")
        self.RF_button.setStyleSheet("background-color: rgb(169,169,169)")

    def hover(self, event):
        # 如果鼠标在Axes对象内部，就检测是否有数据点被悬停，并显示注释框
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            dist1, idx1 = self.tree1.query((x, y), k=1)
            dist2, idx2 = self.tree2.query((x, y), k=1)
            if dist1 < 0.15 or dist2 < 0.15:  # 设置一个距离阈值，避免显示太远的数据点
                if dist1 < dist2:
                    x, y = self.points1[idx1]
                else:
                    x, y = self.points2[idx2]
                self.annot.xy = (x, y)
                text = "{}\nMon1: {:.2f}\nMon2: {:.2f}".format(self.keys[idx1], self.y1[idx1], self.y2[idx2])
                self.annot.set_text(text)
                self.annot.set_visible(True)
                self.canvas.draw_idle()
            else:
                # 如果没有数据点被悬停，就隐藏注释框
                if self.annot.get_visible():
                    self.annot.set_visible(False)
                    self.canvas.draw_idle()

    def tx_select1(self):
        self.name_text = 'TX1'
        return self.name_text

    def tx_select2(self):
        self.name_text = 'TX2'
        return self.name_text

    def LOC_hide(self):
        self.LOC_CL.show()
        self.LOC_DS.show()
        self.LOC_NF.show()
        self.LOC_CLR.show()
        self.GP_CL.hide()
        self.GP_DS.hide()
        self.GP_NF.hide()
        self.GP_CLR.hide()

    def GP_hide(self):
        self.LOC_CL.hide()
        self.LOC_DS.hide()
        self.LOC_NF.hide()
        self.LOC_CLR.hide()
        self.GP_CL.show()
        self.GP_DS.show()
        self.GP_NF.show()
        self.GP_CLR.show()

    def framehide(self):
        if self.stc == 1:
            self.textbrowser.show()
            self.frame.hide()
            self.DDM_button.hide()
            self.SDM_button.hide()
            self.RF_button.hide()
            self.tx1_select.hide()
            self.tx2_select.hide()
            self.stc = 0
        elif self.stc == 0:
            self.textbrowser.hide()
            self.frame.show()
            self.DDM_button.show()
            self.SDM_button.show()
            self.RF_button.show()
            self.tx1_select.show()
            self.tx2_select.show()
            self.stc = 1

    def save_address(self):
        self.data_address.setText(QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "C:\\"))

    def handle_LOC_CL_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.LOC_CL_DDM)
            self.SDM_button.clicked.connect(self.LOC_CL_SDM)
            self.RF_button.clicked.connect(self.LOC_CL_RF)

    def LOC_CL_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                print(self.flag)
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.2, 1.6, 0.4))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5, zorder=0)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.2, 1.6, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                print(self.flag)
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.2, 1.6, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5, zorder=0)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.2, 1.6, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_CL_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(37.5, 44.0, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(37.5, 44, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(37.5, 44.0, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(37.5, 44, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_CL_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.3))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_LOC_DS_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.LOC_DS_DDM)
            self.SDM_button.clicked.connect(self.LOC_DS_SDM)
            self.RF_button.clicked.connect(self.LOC_DS_RF)

    def LOC_DS_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 2.5, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 2.5, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())
                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 2.5, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 2.5, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按


    def LOC_DS_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_DS_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    y3 = round(y3,2)

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 4.4, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    y3 = round(y3,2)

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 4.4, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    y3 = round(y3, 2)

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 4.4, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    y3 = round(y3, 2)

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 4.4, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_LOC_NF_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.LOC_NF_DDM)
            self.SDM_button.clicked.connect(self.LOC_NF_SDM)
            self.RF_button.clicked.connect(self.LOC_NF_RF)

    def LOC_NF_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.3, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.3, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.3, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-1.3, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_NF_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(25, 60, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_NF_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.4, 4.3, 0.4))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.4, 4.3, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.4, 4.3, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.4, 4.3, 0.4))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_LOC_CLR_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.LOC_CLR_DDM)
            self.SDM_button.clicked.connect(self.LOC_CLR_SDM)
            self.RF_button.clicked.connect(self.LOC_CLR_RF)

    def LOC_CLR_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-0.9, 1.2, 0.3))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-0.9, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-0.9, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-0.9, 1.2, 0.3))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_CLR_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(36, 45, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(36, 45, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(36, 45, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 40.0 + low_alarm
                    y4 = 40.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(36, 45, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def LOC_CLR_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'LOC航向' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        if self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX1 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'LOC航向' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'LOC门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.6, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('LOC TX2 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_GP_CL_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.GP_CL_DDM)
            self.SDM_button.clicked.connect(self.GP_CL_SDM)
            self.RF_button.clicked.connect(self.GP_CL_RF)

    def GP_CL_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.0, 4.1, 0.8))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.0, 4.1, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.0, 4.1, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.0, 4.1, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_CL_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75, 86, 1))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75, 86, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75, 86, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75, 86, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_CL_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.62, 3.48, 0.1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.62, 3.48, 0.1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.62, 3.48, 0.1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CL RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CL RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.62, 3.48, 0.1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CL RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_GP_DS_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.GP_DS_DDM)
            self.SDM_button.clicked.connect(self.GP_DS_SDM)
            self.RF_button.clicked.connect(self.GP_DS_RF)

    def GP_DS_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 3.0, 0.8))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 3.0, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 3.0, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-2.0, 3.0, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_DS_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_DS_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.6, 4.4, 0.5))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.6, 4.4, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.6, 4.4, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'DS RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'DS RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.6, 4.4, 0.5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 DS RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_GP_NF_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.GP_NF_DDM)
            self.SDM_button.clicked.connect(self.GP_NF_SDM)
            self.RF_button.clicked.connect(self.GP_NF_RF)

    def GP_NF_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-3, 4.0, 1))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-3, 4.0, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-3, 4.0, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-3, 4.0, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_NF_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(60, 105, 5))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_NF_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 5, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 5, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 5, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'NF RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'NF RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(1.8, 5, 0.8))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 NF RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def handle_GP_CLR_click(self):
        address = self.data_address.text()
        if address != '请选择数据保存路径！' or '':
            self.textbrowser.hide()
            self.stc = 1
            self.DDM_button.disconnect()
            self.SDM_button.disconnect()
            self.RF_button.disconnect()
            self.pushbutton_color()
            self.DDM_button.clicked.connect(self.GP_CLR_DDM)
            self.SDM_button.clicked.connect(self.GP_CLR_SDM)
            self.RF_button.clicked.connect(self.GP_CLR_RF)

    def GP_CLR_DDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.5, 4.5, 1))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.5, 4.5, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)

                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    print(y3, y4)
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.5, 4.5, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR DDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR DDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 0.0 + low_alarm
                    y4 = 0.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(-4.5, 4.5, 1))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR DDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_CLR_SDM(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75.5, 85.5, 1.0))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75.5, 85.5, 1.0))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75.5, 85.5, 1.0))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR SDM.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR SDM.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 80.0 + low_alarm
                    y4 = 80.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(75.5, 85.5, 1.0))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR SDM', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

    def GP_CLR_RF(self):
        address = self.data_address.text()
        self.number = int(self.num.text())
        if self.flag == 0:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:        # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith('.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith('.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.5, 0.2))      # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys     # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机历史数据库' + '\\' + 'GP下滑' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.5, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按
        elif self.flag == 1:
            if self.name_text == 'TX1':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '1号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm
                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.5, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴标签
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX1 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()    # 解除SDM按钮的槽函数，防止多按
            elif self.name_text == 'TX2':
                # 在每次重新运行代码之前，删除旧图形小部件
                try:
                    for i in reversed(range(self.frame.layout().count())):
                        widgetToRemove = self.frame.layout().itemAt(i).widget()
                        # 从布局中删除小部件
                        self.frame.layout().removeWidget(widgetToRemove)
                        # 释放小部件的内存
                        widgetToRemove.setParent(None)
                except:
                    print(1)

                with open(address + '\\' + '2号机实时数据库' + '\\' + 'GP下滑' + '\\' + 'CLR RF.txt', "r") as f:
                    content = f.read()
                # 处理数据库读数
                dict_data = eval(content)
                keys = list(dict_data.keys())
                values = list(dict_data.values())
                # 处理列表数据
                new_list_1 = [x[0] for x in values]  # 取出子元素列表的第一个值
                new_list_2 = [x[1].strip() for x in values]  # 去除子元素列表的第二个值的空格
                mon1 = [x.strip('. ') for x in new_list_1]  # 去除开头和结尾的"."和空格
                mon2 = [x.strip('. ') for x in new_list_2]  # 去除开头和结尾的"."和空格

                try:  # 获取门限值
                    with open(address + '\\' + '门限数据' + '\\' + 'GP门限' + '\\' + 'CLR RF.txt', "r") as f:
                        content = f.read()
                    # 处理数据库读数
                    my_list = content.split(",")
                    low_alarm = my_list[1]
                    high_alarm = my_list[2]
                    if low_alarm.startswith('.') or low_alarm.startswith(' ') or low_alarm.endswith(
                            '.') or low_alarm.endswith(' '):
                        low_alarm = low_alarm.strip('. ')
                    if high_alarm.startswith('.') or high_alarm.startswith(' ') or high_alarm.endswith(
                            '.') or high_alarm.endswith(' '):
                        high_alarm = high_alarm.strip('. ')
                    low_alarm = float(low_alarm)
                    high_alarm = float(high_alarm)
                except:
                    print(111)

                # 绘制图形
                self.frame.setLayout(QVBoxLayout())

                # 创建一个FigureCanvas对象，并添加到布局中
                self.canvas = FigureCanvas(Figure(figsize=(5, 4), dpi=100))
                self.frame.layout().addWidget(self.canvas)

                # 在FigureCanvas对象中创建一个Figure对象
                self.fig = self.canvas.figure

                # 在Figure对象中创建一个Axes对象
                self.ax = self.fig.add_subplot(1, 1, 1)

                # 生成x和y轴
                length = len(keys)
                if length >= self.number:

                    keys = keys[-self.number:]
                    mon1 = mon1[-self.number:]
                    mon2 = mon2[-self.number:]

                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]

                    x = np.array(list(range(self.number)))
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)
                else:
                    x = np.array(list(range(length)))
                    mon1 = [float(x) for x in mon1]
                    mon2 = [float(x) for x in mon2]
                    y1 = np.array(mon1)
                    y2 = np.array(mon2)

                # 红色线条画Mon1折线
                self.ax.plot(x, y1, color='red', linewidth=2, zorder=1, label='Mon1')
                self.ax.scatter(x, y1, zorder=2)
                # 蓝色线条画Mon2折线
                self.ax.plot(x, y2, color='blue', linewidth=2, zorder=1, label='Mon2')
                self.ax.scatter(x, y2, zorder=2)

                # 画上下限
                try:
                    y3 = 3.0 + low_alarm
                    y4 = 3.0 + high_alarm

                    self.ax.axhline(y=y3, color='orange', linewidth=2, label=f'Al.low: {y3}\nAl.high: {y4}')
                    self.ax.axhline(y=y4, color='orange', linewidth=2)
                except:
                    print('1')

                self.ax.set_yticks(np.arange(2.6, 3.5, 0.2))  # 设置纵轴刻度
                self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
                self.ax.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=8)

                x_labels = keys  # 设定横轴的代表值
                self.ax.set_xticks(x)
                self.ax.set_xticklabels(x_labels, rotation=90, fontsize=6)

                # 为Axes对象添加标题和标签
                self.ax.set_position((0.07, 0.25, 0.9, 0.7))
                self.ax.set_title('GP TX2 CLR RF', y=0.9, x=0.5, fontsize=8)

                # 创建一个注释框，并设置为不可见
                self.annot = self.ax.annotate("", xy=(0, 0), xytext=(-25, 17), textcoords="offset points",
                                              bbox=dict(boxstyle="round", fc="w"))
                self.annot.set_visible(False)

                # 连接鼠标移动事件到自定义的函数
                self.canvas.mpl_connect("motion_notify_event", self.hover)

                # 创建一个空间索引树，用于快速查找最近的数据点
                self.y1 = y1
                self.y2 = y2
                self.points1 = np.column_stack((x, y1))
                self.tree1 = spatial.cKDTree(self.points1)
                self.points2 = np.column_stack((x, y2))
                self.tree2 = spatial.cKDTree(self.points2)
                self.keys = list(dict_data.keys())

                # self.SDM_button.disconnect()  # 解除SDM按钮的槽函数，防止多按

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
