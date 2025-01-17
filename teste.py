from clientes import Cliente
from conta import Conta, ContaEspecial
kaue = Cliente("Kaue Barbosa", "555-1234")
francisca = Cliente("Francisca Maria", "444-7897")
conta1 = Conta([kaue], 1,2)
conta2 = ContaEspecial([francisca, kaue], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(30)
conta1.extrato()
conta2.extrato()