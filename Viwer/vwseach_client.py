from Viwer import noname
from Service.svClient import count_client
from DataBase.conection import Client


class SeachClient(noname.seach_client):
    def __init__(self, parent, search):
        noname.seach_client.__init__(self, parent)
        self.search: int = search

    @property
    def search(self) -> int:
        return self.search

    @search.setter
    def search(self, value):
        self._search = value

    def OnbtPesquisaClick(self, event):
        client = Client.select(Client.nome, Client.id, Client.cpf).order_by(Client.id.asc())
        for row in range(count_client()):
            if row > 14:
                self.grid_client.AppendRows(1)
            self.grid_client.SetCellValue(row, 1, client[row].nome)
            self.grid_client.SetCellValue(row, 0, str(client[row].id))
            self.grid_client.SetCellValue(row, 2, client[row].cpf)
        event.Skip()

    def OnDBClickGrid(self, event):
        client = Client.select(Client.id)
        position = self.grid_client.GetGridCursorRow()
        SeachClient.search = int(client[position].id)
        self.Destroy()
        event.Skip()


SeachClient.search = 0
