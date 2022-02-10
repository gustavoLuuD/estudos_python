class Conta:
    # construtor
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print("Conta criada com sucesso")

    def extrato(self):
        print(f"Saldo do titular {self.__titular}: {self.__saldo}")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self,valor):
        self.__saldo -= valor
    
    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)