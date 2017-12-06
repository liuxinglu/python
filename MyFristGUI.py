import wx
import turtle
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
