class Animal:
    def __init__(self, numero_patas, alimento, genero):
        self.numero_patas = numero_patas
        self.alimento = alimento
        self.genero = genero

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
        
class Mamifero(Animal):
    # O **kw representa todas as características da classe Pai, porém, para criar um objeto, você precisa passar os parâmetros nomeados
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    def latir(self):
        print('Auau')

class Passaro(Ave):
    def piar(self):
        print('Piupiu')

cachorro = Cachorro(numero_patas=4, alimento='ração', genero='masculino', cor_pelo='Preto')
print(cachorro)