import wx
from wx import MessageBoxCaptionStr, OK, DefaultPosition
from Class.client import Client
from Service.svClient import new_table, search_cep, count_client
from DataBase.conection import Client as tbClient

from Viwer import noname
from Viwer.vwseach_client import SeachClient
from Viwer.vwclimate import Climate


class RegClient(noname.reg_client):
    def __init__(self, parent):
        noname.reg_client.__init__(self, parent)

    def OnBtClickbt_cancelar(self, event):
        self.Destroy()
        event.Skip()

    def OnBtClickbt_salvar(self, event):
        if self.ed_nome.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o nome!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_nome.SetFocus()

        elif self.ed_cpf.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o CPF!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_cpf.SetFocus()

        elif self.ed_rg.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o RG!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_rg.SetFocus()

        elif self.ed_telefone.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o telefone!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_telefone.SetFocus()

        elif self.ed_cep.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o cep!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_cep.SetFocus()

        elif self.ed_rua.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher a rua!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_rua.SetFocus()

        elif self.ed_numero.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o número!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_numero.SetFocus()

        elif self.ed_bairro.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher o bairro!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_bairro.SetFocus()

        elif self.ed_cidade.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher a cidade!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_cidade.SetFocus()

        elif self.ed_uf.GetValue() == '':
            wx.MessageDialog(None,
                             message=f'Você deve preencher a UF!',
                             caption=MessageBoxCaptionStr,
                             style=OK,
                             pos=DefaultPosition).ShowModal()
            self.ed_uf.SetFocus()

        Client.id = self.ed_codigo.GetValue()
        Client.nome = self.ed_nome.GetValue()
        Client.cpf = self.ed_cpf.GetValue()
        Client.telefone = self.ed_telefone.GetValue()
        Client.rg = self.ed_rg.GetValue()
        Client.logradouro = self.ed_rua.GetValue()
        Client.bairro = self.ed_bairro.GetValue()
        Client.numero = self.ed_numero.GetValue()
        Client.localidade = self.ed_cidade.GetValue()
        Client.uf = self.ed_uf.GetValue()
        Client.cep = self.ed_cep.GetValue()
        new_table()
        event.Skip()

    def OnKillFocusEd_cep(self, event):
        search = search_cep(self.ed_cep.GetValue())
        self.ed_bairro.SetValue(search['bairro'])
        self.ed_rua.SetValue(search['logradouro'])
        self.ed_cidade.SetValue(search['localidade'])
        self.ed_uf.SetValue(search['uf'])
        event.Skip()

    def OnActiveClient(self, event):
        self.ed_codigo.SetValue(str(count_client() + 1))
        search = SeachClient.search
        self.ed_nome.SetFocus()
        if search > 0:
            client = tbClient.select(tbClient.id,
                                     tbClient.nome,
                                     tbClient.cpf,
                                     tbClient.telefone,
                                     tbClient.rg,
                                     tbClient.logradouro,
                                     tbClient.bairro,
                                     tbClient.numero,
                                     tbClient.localidade,
                                     tbClient.uf,
                                     tbClient.cep).where(tbClient.id == search)
            self.ed_codigo.SetValue(str(client[0].id))
            self.ed_nome.SetValue(client[0].nome)
            self.ed_cpf.SetValue(client[0].cpf)
            self.ed_telefone.SetValue(client[0].telefone)
            self.ed_rg.SetValue(client[0].rg)
            self.ed_rua.SetValue(client[0].logradouro)
            self.ed_bairro.SetValue(client[0].bairro)
            self.ed_numero.SetValue(client[0].numero)
            self.ed_cidade.SetValue(client[0].localidade)
            self.ed_uf.SetValue(client[0].uf)
            self.ed_cep.SetValue(client[0].cep)
        event.Skip()

    def OnBtPesquisaClick(self, event):
        app = wx.App()
        frame = SeachClient(None, search='')
        frame.Show()
        app.MainLoop()
        event.Skip()

    def OnBtClimaClick(self, event):
        Climate.cidade = self.ed_cidade.GetValue()
        Climate.uf = self.ed_uf.GetValue()
        app = wx.App()
        frame = Climate(None, Climate.uf, Climate.cidade)
        frame.Show()
        app.MainLoop()
        event.Skip()



