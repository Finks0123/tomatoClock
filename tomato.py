# coding:utf-8
"""
@author:Finks
@time:2022/6/23 14:16

番茄闹钟
"""

from tkinter import *
from tkinter import messagebox

tomato_time = 25
break_time = 5
#

class TomatoClock():
    def __init__(self):
        self.count = 0
        self.rest = False
        self.work = True
        self.epoch = 0
        pass

    def notify_me(self, msg):
        """
        窗口显示消息
        :param msg:
        :return:
        """
        try:
            root = Tk()
            root.withdraw()  # ****实现主窗口隐藏
            root.wm_attributes('-topmost', 1)
            messagebox.showinfo('提示', msg)
        except:
            pass

    def tomato_on_time(self):
        self.count += 1
        # print(self.count, self.work, self.rest)
        if self.count % (tomato_time * 60) == 0 and self.work:
            self.work = False
            self.rest = True
            self.count = 0
            self.epoch += 1
            self.notify_me(f'你已经完成【{self.epoch}】轮Tomato！ 做的很好！ 现在休息5分钟！')

        if self.count % (break_time * 60) == 0 and self.rest:
            self.rest = False
            self.work = True
            self.count = 0
            self.notify_me('休息结束！集中注意力进入下一轮tomato!')
        pass


if __name__ == "__main__":
    obj = TomatoClock()
    obj.notify_me('s')
