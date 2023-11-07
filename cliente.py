
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property # É como um get. Só funciona com atributos privados
    def nome(self):
        return self.__nome.title() # O title retorna com a primeira letra maiúscula

    @nome.setter
    del nome(self, nome):
        self.__nome = nome

