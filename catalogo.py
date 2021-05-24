class Musica:

    def __init__(self, nome, ano, album, id):
        self.__nome = nome
        self.__ano = ano
        self.__album = album
        self.__id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def album(self):
        return self.__album
    @album.setter
    def album(self, novo_album):
        self.__album = novo_album

    def __str__(self):
        return f'''Nome: {self.__nome}\nAno:{self.__ano}\nÁlbum:{self.__album}\nID: {self.__id}'''


if __name__ == '__main__':
    m1 = Musica("We Are", 1998, "One piece", 0)

    print(m1)