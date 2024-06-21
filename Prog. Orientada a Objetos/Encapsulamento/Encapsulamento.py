# Encapsulamento é usado para proteção de acesso a variáveis e métodos, para evitar a modificação acidental de dados
# Variável Pública: Pode ser acessado de fora da classe
# Variável Privada: Só pode ser acessado pela própria classe

class Conta:
    def __init__(self, numero_agencia, saldo=0):
        # '_saldo' é uma variável privada, por começar com um UNDERLINE
        self.numero_agencia = numero_agencia
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    # A forma correta de acessar uma variável privada é usando um método:
    def mostrar_saldo(self):
        return self._saldo

# O UNDERLINE no início da variável ou método não faz com que ela deixe de poder ser acessada, porém, é uma convenção na comunidade de que não é correto acessar essa variável.

conta = Conta('0001', 100)
conta.depositar(100)
# Essa é a maneira correta de acessar a variável.
print(conta.mostrar_saldo())
# Essa é a maneira incorreta. Funciona, porém, essa variável não deveria ser acessada.
print(conta._saldo)