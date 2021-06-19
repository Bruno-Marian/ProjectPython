import wx
from Viwer import noname
from Viwer.vwreg_client import RegClient
from Viwer.vwconfig_db import Configdb
from Viwer.vwrel_client import RelClient


class Menu(noname.menu):
    def __init__(self, parent):
        noname.menu.__init__(self, parent)

    def OnBtClickbt_cadastro(self, event):
        app = wx.App()
        frame = RegClient(None)
        frame.Show()
        app.MainLoop()
        event.Skip()

    def OnBtClickbt_configdb(self, event):
        app = wx.App()
        frame = Configdb(None)
        frame.Show()
        app.MainLoop()
        event.Skip()

    def OnBtClickbt_rel(self, event):
        app = wx.App()
        frame = RelClient(None)
        frame.Show()
        app.MainLoop()
        event.Skip()
