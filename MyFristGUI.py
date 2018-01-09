# -*- coding: UTF-8 -*-
# import wx
# import turtle
# import pickle
from graphics import *

# class MyFirstGUI(wx.Frame):
#     def __init__(self, *args, **kw):
#         super(MyFirstGUI, self).__init__(*args, **kw)
#         pnl = wx.Panel(self)

#         staticText = wx.StaticText(pnl, label = "hello world", pos = (25, 25))
#         font = staticText.GetFont()
#         font.PointSize += 10
#         font = font.Bold()
#         staticText.SetFont(font)

#         self.makeMenuBar()
#         self.CreateStatusBar()
#         self.SetStatusText("welcome to wxPython")

#     # def accelerator(self):
#     #     entries = [wx.AcceleratorEntry() for i in xrange(3)]
#     #     # entries[0].Set(wx.ACCEL_CTRL, 'N', ID_NEW_WINDOW)
#     #     entries[0].Set(wx.ACCEL_CTRL, 'X', wx.ID_EXIT)
#     #     entries[1].Set(wx.ACCEL_SHIFT, 'A', wx.ID_ABOUT)
#     #     entries[2].Set(wx.ACCEL_NORMAL, wx.WXK_DELETE, wx.ID_CUT)

#     #     accel = wx.AcceleratorTable(entries)
#     #     self.SetAcceleratorTable(accel)

#     def makeMenuBar(self):
#         fileMenu = wx.Menu()
#         helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item")
#         fileMenu.AppendSeparator()
#         exitItem = fileMenu.Append(wx.ID_EXIT)
#         helpMenu = wx.Menu()
#         aboutItem = helpMenu.Append(wx.ID_ABOUT)
#         menuBar = wx.MenuBar()
#         menuBar.Append(fileMenu, "&File")
#         menuBar.Append(helpMenu, "&Help")

#         self.SetMenuBar(menuBar)

#         self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
#         self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
#         self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

#     def OnExit(self, event):
#         self.Close(True)
    
#     def OnHello(self, event):
#         wx.MessageBox("Hello again from wxPython")

#     def OnAbout(self, event):
#         wx.MessageBox("This is a wxPython Hello world sample", "About Hello world 2", wx.OK|wx.ICON_INFORMATION)

#     def savefile(self):
#         game_data = {'player_position': 'N23 E45',
#         'pockets': ['keys', 'pocket knife', 'polished stone'],
#         'backpack': ['rope', 'hammer', 'apple'],
#         'money': 158.03}
#         save_file = open('/Users/star_xlliu/save.txt', 'wb')
#         pickle.dump(game_data, save_file)
#         save_file.close()
#         load_file = open('/Users/star_xlliu/save.txt', 'rb')
#         load_game_data = pickle.load(load_file)
#         load_file.close()
#         print(load_game_data['money'])


def main():
    win = GraphWin("draw", 500, 500)
    # win.setCoords(0, 0, 500, 500) 变换坐标左上角右下角
    # win.setCoords(0, 0, 3.0, 4.0) #按比例转换坐标
    message = Text(Point(250, 10), "点击四方")
    message.draw(win)

    leftEye = Circle(Point(80, 80), 5)
    leftEye.setFill("yellow")
    leftEye.setOutline("red")
    rightEye = leftEye.clone()
    rightEye.move(40, 0)
    leftEye.draw(win)
    rightEye.draw(win)
    face = Circle(Point(100, 95), 50)
    mouth = Line(Point(80, 110), Point(120, 110))
    face.draw(win)
    mouth.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)

    polygon = Polygon(p1, p2, p3, p4)
    polygon.setFill("red")
    polygon.setOutline("black")
    polygon.draw(win)
    #体会Text和Entry的区别，前者只能由程序输入内容，后者可以在图形界面输入内容；两者都是用getText()获取内容，用setText()展示内容。
    Text(Point(200, 100), "Celsius Temperature:").draw(win)
    Text(Point(200, 150), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(300, 100), 5) #前面是位置， 后面是宽度 可以写数字
    input.setText("0.0")
    input.draw(win)

    output = Text(Point(300, 150), "")
    output.draw(win)

    button = Text(Point(250, 250), "Convert It") #按钮字样
    button.draw(win)
    Rectangle(Point(230, 270), Point(300, 220)).draw(win)

    win.getMouse()
    celsius = eval(input.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32.0

    output.setText(fahrenheit)
    button.setText("Quit")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
    # app = wx.App()
    # frm = MyFirstGUI(None, title='Hello world 3')
    # frm.Show()
    # app.MainLoop()
