import wx
import wx.adv

from tomato import TomatoClock
from utils import get_iter, rand_a_name


class MyTaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self, parent):
        super(MyTaskBarIcon, self).__init__()

        self.img_iter = get_iter('dark_cat')

        self.id_quit = wx.NewId()
        self.switch_icon_id = wx.NewId()


        # 任务栏包含两个定时任务：更新图标和启动弹窗
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_icon, self.timer)
        self.timer.Start(50)  # 50ms启动一次

        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.pop_window, self.timer2)
        self.timer2.Start(1000)  # 1s启动一次事件

        # 绑触发事件
        self.Bind(wx.EVT_MENU, parent.quit_app, id=self.id_quit)
        self.Bind(wx.EVT_MENU, self.switch_icon, id=self.switch_icon_id)

        self.tomato = TomatoClock()

    def CreatePopupMenu(self):
        """创建菜单"""
        self.menu = wx.Menu()
        self.menu.Append(self.id_quit, "退出")
        self.menu.Append(self.switch_icon_id, "switch")
        return self.menu

    def update_icon(self, evt):
        # 读取图片
        self.SetIcon(wx.Icon(self.img_iter.__next__()), '番茄闹钟')

    def pop_window(self, evt):
        self.tomato.tomato_on_time()

    def switch_icon(self, evt):
        name = rand_a_name()
        self.img_iter = get_iter(name)
        pass


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(None)

        self.task_bar_icon = MyTaskBarIcon(self)

    def quit_app(self, evt):
        '''退出主程序操作'''
        self.task_bar_icon.Destroy()
        wx.CallAfter(self.Destroy)


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame()
    app.MainLoop()
