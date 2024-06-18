# Apresentando classes
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        # Setar as características
        self.nome = nome
        self.cor = cor
        # Por padrão a característica acordado é definida como True
        self.acordado = acordado
    
    def latir(self):
        print('AuAu')

    def dormir(self):
        # Quando o cachorro dorme, a característica acordado é definida como False
        self.acordado = False
        print('ZZzzzz....')

# Após criar a classe cachorro, preciso instaciar objetos usando a classe

cachorro_1 = Cachorro('Chappie', 'amarelo', False) # Chappie está dormindo
cachorro_2 = Cachorro('Aladim', 'branco e preto') # Aladim está acordado

# Ao chamar o objeto usando ".funcão", eu chamo a funcão da classe, definida anteriormente 
cachorro_1.latir()

# Vejo se o cachorro está acordado
print(cachorro_2.acordado)
# O coloco para dormir
cachorro_2.dormir()
# Verifico novamente
print(cachorro_2.acordado)


# DESAFIO
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, andando=False):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.andando = andando

    # Traz as informacões sobre a bicicleta desejada
    '''
    def __str__(self):
        return f'{self.__class__.__name__}: \nCor: {self.cor} \nModelo: {self.modelo} \nAno: {self.ano} \nValor: {self.valor}'
    '''

    # funcão str melhorada
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    def buzinar(self):
        print('BIBI')

    def andar(self):
        if self.andando == False:
            self.andando = True
            print('Bicicleta andou!')
        else:
            print('Bicicleta já está andando!')

    def parar(self):
        if self.andando == False:
            print('A bicicleta já está parada!')
        else:
            print('Bicicleta parou!')


bicicleta_1 = Bicicleta('vermelha', 'caloi', 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.andar()
bicicleta_1.parar()

# "Chama" a funcão __str__
print(bicicleta_1)
