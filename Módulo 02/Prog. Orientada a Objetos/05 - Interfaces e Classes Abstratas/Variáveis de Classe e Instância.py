class Estudante:
    # Essa é uma variável de classe, padrão em TODOS os objetos
    escola = 'DIO'

    # E essas são variáveis de instância, padrão em só um dos objetos
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome}, {self.matricula} - {self.escola}"
    
Guilherme = Estudante('Guilherme', 56451)
Giovana = Estudante('Giovana', 17323)
print(f'{Guilherme}\n{Giovana}')

# Posso também trocar a variável de classe dessa forma, assim mudando em todos os objetos
Estudante.escola = 'Python'
print(f'{Guilherme}\n{Giovana}')