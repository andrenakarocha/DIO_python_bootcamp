class Foo:
    def __init__(self, x=None):
        self._x = x

    # O @property faz com que você consiga acessar um método com a sintaxe de atributo
    @property
    def x(self):
        return self._x or 0

    # o setter é usado para setar valores na propriedade
    @x.setter
    def x(self, valor):
        self._x += valor      

    @x.deleter
    def x(self):
        self._x -= 1
    
    
# Perceba que eu uso a sintaxe de atributo para acessar um método, e por causa do @property, o código funciona
foo = Foo(10)
print(foo.x)
# Estou usando o atributo setter para somar mais 10 no x
foo.x = 10
print(foo.x)
# Estou usando o atributo deleter para diminuir 1 no x
del foo.x
print(foo.x)


# Exemplo real de uso do @property
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        # Essa lógica por exemplo, não faz sentido usar o property, porém, usamos para o exemplo.
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa('Guilherme', 1994)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')

# Isso é só um exemplo. Quando você tem uma situação onde não vai criar setters para as propriedades, não há sentido em criar várias propriedades, apenas deixe o atributo
# público e acesse diretamente pelo nome.