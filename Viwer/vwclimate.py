from Viwer import noname
from Service.svClient import search_climate


class Climate(noname.climate):
    def __init__(self, parent, uf, cidade):
        noname.climate.__init__(self, parent)
        self.uf = uf
        self.cidade = cidade

    @property
    def uf(self):
        return self.uf

    @property
    def cidade(self):
        return self.cidade

    @uf.setter
    def uf(self, value):
        self._uf = value

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    def bt_Click_sair(self, event):
        self.Destroy()
        event.Skip()

    def OnActivateClimate(self, event):
        search = search_climate(Climate.cidade, Climate.uf)
        self.TextCtrlClimate.SetValue(f"O clima para {search['city']} em {search['date']}: \n\n"
                                      f"Tempo: {search['description']}\n"
                                      f"Humidade de: {search['humidity']}º\n"
                                      f"Temperatura de: {search['temp']}º\n"
                                      f"Nascer do sol em: {search['sunrise']}\n"
                                      f"Pôr do sol em: {search['sunset']}")
        event.Skip()


