from DataBase.conection import Client
from Service.svClient import count_client
from Viwer import noname


class RelClient(noname.rel_client):
    def __init__(self, parent):
        noname.rel_client.__init__(self, parent)

    def OnActiveRel(self, event):
        self.Maximize()
        client = Client.select(Client.nome, Client.id, Client.cpf, Client.telefone, Client.rg, Client.logradouro,
                               Client.bairro, Client.numero, Client.localidade, Client.uf, Client.cep,
                               Client.created_date)
        for row in range(count_client()):
            if row > 5:
                self.grid_rel.AppendRows(1)
            self.grid_rel.SetCellValue(row, 0, str(client[row].id))
            self.grid_rel.SetCellValue(row, 1, client[row].nome)
            self.grid_rel.SetCellValue(row, 2, client[row].cpf)
            self.grid_rel.SetCellValue(row, 3, client[row].telefone)
            self.grid_rel.SetCellValue(row, 4, client[row].rg)
            self.grid_rel.SetCellValue(row, 5, client[row].logradouro)
            self.grid_rel.SetCellValue(row, 6, client[row].bairro)
            self.grid_rel.SetCellValue(row, 7, client[row].numero)
            self.grid_rel.SetCellValue(row, 8, client[row].localidade)
            self.grid_rel.SetCellValue(row, 9, client[row].uf)
            self.grid_rel.SetCellValue(row, 10, client[row].cep)
            self.grid_rel.SetCellValue(row, 11, str(client[row].created_date))
            self.grid_rel.AutoSize()
        event.Skip()
