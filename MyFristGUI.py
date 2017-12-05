import wx
import turtle
import copy
import pickle

class MyFirstGUI(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFirstGUI, self).__init__(*args, **kw)
        pnl = wx.Panel(self)

        staticText = wx.StaticText(pnl, label = "hello world", pos = (25, 25))
        font = staticText.GetFont()
        font.PointSize += 10
        font = font.Bold()
        staticText.SetFont(font)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("welcome to wxPython")

    # def accelerator(self):
    #     entries = [wx.AcceleratorEntry() for i in xrange(3)]
    #     # entries[0].Set(wx.ACCEL_CTRL, 'N', ID_NEW_WINDOW)
    #     entries[0].Set(wx.ACCEL_CTRL, 'X', wx.ID_EXIT)
    #     entries[1].Set(wx.ACCEL_SHIFT, 'A', wx.ID_ABOUT)
    #     entries[2].Set(wx.ACCEL_NORMAL, wx.WXK_DELETE, wx.ID_CUT)

    #     accel = wx.AcceleratorTable(entries)
    #     self.SetAcceleratorTable(accel)

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)
    
    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample", "About Hello world 2", wx.OK|wx.ICON_INFORMATION)
    
    def drawGra2(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        i = 0
        for i in list(range(0, 4)):
            t.up()
            t.forward(10)
            t.down()
            t.forward(30)
            t.up()
            t.forward(10)
            t.left(90)
            i = i + 1
        t.reset()
        while i < 6:
            t.backward(100)
            t.up()
            t.right(90)
            t.forward(20)
            t.left(90)
            t.down()
            t.forward(100)
            i = i + 1
        while i < 360:
            t.down()
            t.right(1)
            t.forward(1)
            i = i + 1
        t.up()
        de = "i value is "
        if i == 360:
            de = de + str(i)
            self.contents.set(de)
        else:
            self.contents.set(de)

    def drawGra(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        t.pencolor('red')
        r = 1
        i = 0
        while i < 180:
            self.drawCircle(t, r)
            r = r + 0.1
            t.left(6)
            i = i + 1
        t.bye()
    
    def drawCircle(self, t_pen, r_num):
        i_circle = 0
        t_pen.down()
        while i_circle < 36:
            t_pen.left(10)
            t_pen.forward(r_num)
            i_circle = i_circle + 1
        t_pen.up()

    def drawFlower(self, flowerNum, jiaodu, r):
        pen_flower = turtle.Pen()
        pen_flower.down()
        while r > 2:
            i_n = 0
            while i_n < flowerNum:
                i_t = 0
                while i_t < 18:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / 18)
                    i_t = i_t + 1
                pen_flower.right(180 - jiaodu)
                i_t = 0
                while i_t < 18:
                    pen_flower.forward(r)
                    pen_flower.right(jiaodu / 18)
                    i_t = i_t + 1
                pen_flower.right(180 - jiaodu)
                pen_flower.right(360 / flowerNum)
                i_n = i_n + 1
            r = r - 0.5
        pen_flower.bye()

    def savefile(self):
        game_data = {'player_position': 'N23 E45',
        'pockets': ['keys', 'pocket knife', 'polished stone'],
        'backpack': ['rope', 'hammer', 'apple'],
        'money': 158.03}
        save_file = open('/Users/star_xlliu/save.txt', 'wb')
        pickle.dump(game_data, save_file)
        save_file.close()
        load_file = open('/Users/star_xlliu/save.txt', 'rb')
        load_game_data = pickle.load(load_file)
        load_file.close()
        print(load_game_data['money'])


    

if __name__ == '__main__':
    app = wx.App()
    frm = MyFirstGUI(None, title='Hello world 3')
    frm.Show()
    app.MainLoop()
