import wx
from wx import MessageBoxCaptionStr, OK, DefaultPosition

from Service.svConection import load_config_database, set_conect
from DataBase.conection import run_conection
from Viwer.vwmenu import Menu


def main():
    app = wx.App()
    frame = Menu(None)
    frame.Show()
    try:
        load_config_database()
        set_conect()
        run_conection()
    except Exception as ex:
        wx.MessageDialog(None,
                         message=f'Você ainda não setou o banco da dados ou as informações estão incorretas: {ex!r}',
                         caption=MessageBoxCaptionStr,
                         style=OK,
                         pos=DefaultPosition).ShowModal()
    app.MainLoop()


if __name__ == '__main__':
    main()

