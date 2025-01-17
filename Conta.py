class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f}")
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            print("verdadeiro")
        else:
            print("falso")
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["Depósito", valor])

    def extrato(self):
        print(f"Extrato CC N {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n   Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            print("verdadeiro")
        else:
            print("falso")

    def extrato(self):
        print(f"Extrato CC N {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        total_disponivel = self.saldo + self.limite
        print(f"\n   Saldo: {self.saldo:10.2f}")
        print(f"   Limite: {self.limite:10.2f}")
        print(f"   Total disponivel para saque: {total_disponivel:10.2f}\n")
