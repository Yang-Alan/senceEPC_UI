import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import random
import threading
import time


################################################
#######创建主窗口
############################################    ####
class MainWindow(QMainWindow):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('senceEPC')
        self.showMaximized()
        global timer
        timer = threading.Timer(1, self.fun_timer)  # 首次启动
        timer.start()

        #####放入WebEngineView
        self.webview = WebEngineView()
        self.setCentralWidget(self.webview)
        self.webview.load(QUrl("file:///C:/Users/Alan/Desktop/python/UI/bar1.html"))

        #####web页面加载完毕，调用函数

        self.webview.page().loadFinished.connect(self.run_js)

    ########运行js脚本，没有回调########
    def run_js(self):
        self.data1 = self.generateData()
        self.data2 = self.generateData()
        self.jscode1 = "getJson1({})".format(self.data1)
        self.jscode2 = "getJson2({})".format(self.data2)
        self.webview.page().runJavaScript(self.jscode1)
        self.webview.page().runJavaScript(self.jscode2)

    def generateData(self):
        return [{
            "name": "Mon",
            "value": random.randint(0, 99)
        }, {
            "name": "Tue",
            "value": random.randint(0, 99)
        }, {
            "name": "Wed",
            "value": random.randint(0, 99)
        }, {
            "name": "Thu",
            "value": random.randint(0, 99)
        }, {
            "name": "Fri",
            "value": random.randint(0, 99)
        }, {
            "name": "Sat",
            "value": random.randint(0, 99)
        }, {
            "name": "Sun",
            "value": random.randint(0, 99)
        }]

    def fun_timer(self):
        self.run_js()
        timer = threading.Timer(1,self.fun_timer)  # 1秒调用一次函数
        # 定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名

        timer.start()  # 启用定时器




################################################
#######创建浏览器
################################################
class WebEngineView(QWebEngineView):
    windowList = []

    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()
        new_window = MainWindow()
        new_window.setCentralWidget(new_webview)
        # new_window.show()
        self.windowList.append(new_window)  # 注：没有这句会崩溃
        return new_webview


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())