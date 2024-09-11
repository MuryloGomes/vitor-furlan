#%%
from cliente import Cliente
from pix import Pix
#%%
# Programa principal
cliente1 = Cliente("Maria", "123.456.789-00", 1000.0)
cliente2 = Cliente("João", "987.654.321-00", 500.0)

print(
    f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}"
)  # Saldo do cliente Maria: R$1000.0

print(
    f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}"
)  # Saldo do cliente João: R$500.0


cliente1.realizar_pix(200.0, cliente2)

print(
    f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}"
)  # Saldo do cliente Maria: R$800.0

print(
    f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}"
)  # Saldo do cliente João: R$700.0


extrato_c1 = cliente1.get_extrato()
for pix in extrato_c1:
    pix.exibir_informacoes()
# Remetente: 123.xxx.xxx-00
# Destinatário: 987.xxx.xxx-00
# Valor: R$200.0

extrato_c2 = cliente2.get_extrato()
for pix in extrato_c2:
    pix.exibir_informacoes()
# Remetente: 123.xxx.xxx-00
# Destinatário: 987.xxx.xxx-00
# Valor: R$200.0


cliente2.realizar_pix(9000.0, cliente1)
# Saldo insuficiente para realizar a transferência.
# %%
