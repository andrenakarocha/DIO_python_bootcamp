class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f'{self.nome} - {self.idade} Anos'

    # Esse é um método de classe
    # Usamos o 'cls' pois é uma convenção ao usar o classmethod
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    # Esse é um método estático, usado para auxiliar
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


pessoa = Pessoa.criar_de_data_nascimento(1994, 3, 21, 'Guilherme')
print(pessoa)

print(Pessoa.maior_idade(14))
print(Pessoa.maior_idade(28))