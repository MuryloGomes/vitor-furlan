#%%
from pix import Pix
#%%
class Cliente:
    def __init__(self, nome: str, cpf: str, saldo: float):
        self.nome = nome
        self.__extrato = []
        self.__cpf = cpf
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def get_extrato(self):
        return self.__extrato
    
    def get_cpf(self):
        return f'{self.__cpf[:3]}.xxx.xxx-{self.__cpf[-2:]}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def retirar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente para retirada.")

    def realizar_pix(self, valor, destinatario):
        if self.__saldo >= valor:
            transacao = Pix(self, destinatario, valor)
            transacao.executar()
            self.registrar_transacao(transacao)
            destinatario.registrar_transacao(transacao)
        else:
            print("Saldo insuficiente para realizar a transferência.")
            
    def registrar_transacao(self, transacao):
        self.__extrato.append(transacao)
# %%
