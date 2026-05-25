class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado")
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print("Saque realizado")

    def exibir_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Leo")
conta.depositar(100)
conta.sacar(30)
conta.exibir_saldo()