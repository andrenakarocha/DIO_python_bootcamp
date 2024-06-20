# Hands-On, Herança Simples
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    def ligar_motor(self):
        print('Ligando o motor')

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    # Mesmo herdando certas características da Classe pai, você pode criar características e funções individuais
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        # O super mantém as características originais, para extender as características dos filhos
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print('Caminhão está carregado!' if self.carregado else 'Caminhão não está carregado!')

    def carregar(self):
        if self.carregado == True:
            print('Caminhão já está carregado!')
        else:
            self.carregado = True
            print('Caminhão carregado!')

    def descarregar(self):
        if self.carregado == False:
            print('Caminhão já está descarregado!')
        else:
            self.carregado = False
            print('Caminhão descarregado!')



moto = Moto('preta', 'abc-1234', 2)
# moto.ligar_motor()
print(moto)

carro = Carro('branco', 'dfg-5678', 4)
# carro.ligar_motor()
print(carro)

caminhao = Caminhao('roxo', 'hij-9101', 8)
# caminhao.ligar_motor()
# caminhao.esta_carregado()
print(caminhao)