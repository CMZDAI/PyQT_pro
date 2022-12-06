# coding = utf-8
# Author: Happy curiosity
# Write time：2022/10/6 11:23
# Dear Egger
# File : qt_1.py

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from login import Ui_Form

class MyMainForm(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.login_Button.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        self.cancel_Button.clicked.connect(self.close)

    def display(self):
        # 利用line Edit控件对象text()函数获取界面输入
        username=self.user_lineEdit.text()
        password=self.pwd_lineEdit.text()
        print(username)
        # 利用text Browser控件对象setText()函数设置界面显示
        self.user_textBrowser.setText("登录成功!\n" + "用户名是: " + username + ",密码是： " + password)

if __name__ == '__main__':
    ##固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app=QApplication(sys.argv)
    ##初始化
    myWin=MyMainForm()
    ##将窗口控件显示在屏幕上
    myWin.show()
    ##程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())