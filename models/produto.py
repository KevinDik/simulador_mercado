from utils.helper import formata_strin


class Produto:
    contador = 1

    def __init__(self, nome, preco):
        self.__codigo = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return f'codigo: {self.codigo} \nnome: {self.nome} preço: {formata_strin(self.preco)}'
