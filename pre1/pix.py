from cliente import Cliente

class Pix:
    def __init__(self, remetente: Cliente, destinatario: Cliente, valor: float):
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__valor = valor

    def executar(self):
        # Deduz do remetente e adiciona ao destinatário
        self.__remetente.retirar(self.__valor)
        self.__destinatario.depositar(self.__valor)

    def exibir_informacoes(self):
        print(f"Remetente: {self.__remetente.get_cpf()}")
        print(f"Destinatário: {self.__destinatario.get_cpf()}")
        print(f"Valor: R${self.__valor}")
