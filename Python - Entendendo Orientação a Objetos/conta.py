
class Conta:
    def __init__(self, numero, titular, saldo, limite): # Função especial para construir o objeto. Self é a referência para encontrar o objeto na memória
        # Adiciona o nome dos parâmetros no __init__ porque queremos que os dados sejam alterados, se um parâmetro for ter um valor padrão, definomos como: limite = 1000.0
        print("Construindo o objeto...{}".format(self))
        self.__numero = numero # cria o atributo numero e define sua característica
        self.__titular = titular
        self.__saldo = saldo # Inserir os 2 __ torna o atributo privado
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # Método privado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, destino): # Omite o origem, por ser usado o self em seu lugar
        self.saca(valor) # Pode ser chamado outro método a partir do self
        destino.deposita(valor)

    @property
    def saldo(self): # Getters apenas retornam o valor dos atributos
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite # Setters são usados para atribuir novos valores aos atributos

    @staticmethod # Métodos estáticos
    def codigo_banco():
        return "001" # O valor é fixo para todos os objetos

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
