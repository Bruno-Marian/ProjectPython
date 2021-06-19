import wx
from wx import MessageBoxCaptionStr, OK, DefaultPosition
from Service.svConection import load_config_database, set_conect, json_create
from Viwer import noname
from Class.conect import Conect
from DataBase.conection import run_conection


class Configdb(noname.config_db):
    def __init__(self, parent):
        noname.config_db.__init__(self, parent)

    def OnBtClickbt_cancelar(self, event):
        self.Destroy()
        event.Skip()

    def OnBtClickbt_salvar(self, event):
        if self.ed_db_name.GetValue() == '':
            self.ed_db_name.SetValue('postgres')

        if self.ed_host.GetValue() == '':
            self.ed_host.SetValue('localhost')

        if self.ed_password.GetValue() == '':
            self.ed_password.SetValue('postgres')

        if self.ed_port.GetValue() == '':
            self.ed_port.SetValue('5432')

        if self.ed_user.GetValue() == '':
            self.ed_user.SetValue('postgres')

        try:
            Conect.db_name = self.ed_db_name.GetValue()
            Conect.host = self.ed_host.GetValue()
            Conect.password = self.ed_password.GetValue()
            Conect.port = self.ed_port.GetValue()
            Conect.user = self.ed_user.GetValue()
            json_create()
            load_config_database()
            set_conect()
            run_conection()
            wx.MessageDialog(None, message=f'Parametros salvos com sucesso', caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
        except Exception as ex:
            wx.MessageDialog(None, message=f'Ocorreu um erro: {ex!r}', caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
        event.Skip()

    def OnActiveConfgDB(self, event):
        self.ed_db_name.SetFocus()
        if not Conect.db_name == '':
            self.ed_db_name.SetValue(Conect.db_name)
            self.ed_host.SetValue(Conect.host)
            self.ed_port.SetValue(Conect.port)
            self.ed_user.SetValue(Conect.user)
            self.ed_password.SetValue(Conect.password)
        event.Skip()


