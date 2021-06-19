class Client:

    def __init__(self,
                 id: int,
                 nome: str,
                 cpf: str,
                 telefone: str,
                 rg: str,
                 logradouro: str,
                 bairro: str,
                 numero: str,
                 localidade: str,
                 uf: str,
                 cep: str):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__rg = rg
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__numero = numero
        self.__localidade = localidade
        self.__uf = uf
        self.__cep = cep

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def rg(self):
        return self.__rg

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def bairro(self):
        return self.__bairro

    @property
    def numero(self):
        return self.__numero

    @property
    def localidade(self):
        return self.__localidade

    @property
    def uf(self):
        return self.__uf

    @property
    def cep(self):
        return self.__cep

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.id = value

    @nome.setter
    def nome(self, value):
        self.nome = value

    @cpf.setter
    def cpf(self, value):
        self.cpf = value

    @telefone.setter
    def telefone(self, value):
        self.telefone = value

    @rg.setter
    def rg(self, value):
        self.rg = value

    @logradouro.setter
    def logradouro(self, value):
        self.logradouro = value

    @bairro.setter
    def bairro(self, value):
        self.bairro = value

    @numero.setter
    def numero(self, value):
        self.numero = value

    @localidade.setter
    def localidade(self, value):
        self.localidade = value

    @uf.setter
    def uf(self, value):
        self.uf = value

    @cep.setter
    def cep(self, value):
        self.cep = value

