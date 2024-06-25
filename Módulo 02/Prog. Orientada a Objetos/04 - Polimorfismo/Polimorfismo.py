# Usando polimorfismo, você pode alterar um método de uma classe pai, na classe filha.
class Ave:
    def __init__(self, cor_pena, cor_bico):
        cor_pena = cor_pena
        cor_bico = cor_bico

    def voar(self):
        print('Voando...')

class Pardal(Ave):
    # Nesse caso, o Pardal consegue voar, então usamos o super para chamar a função do pai
    def voar(self):
        super().voar()

class Galinha(Ave):
    def voar(self):
        print('Galinha não voa')

# O polimorfismo entra aqui. Usamos outra função para chamar o método voar, assim não interferindo.
def plano_de_voo(ave):
    ave.voar()

plano_de_voo(Pardal('preta', 'amarelo'))
plano_de_voo(Galinha('branca', 'laranja'))