class Cachorro:
    
    # Método Construtor
    # Sempre executado no início 
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Método Destrutor
    # Sempre executado no final
    def __del__(self):
        print('Destruindo a instância')

def criar_cachorro(nome, cor, acordado):
    cachorro = Cachorro(nome, cor, acordado)
    return cachorro

cachorro = criar_cachorro('Zeus', 'preto', True)

print('a')
# Destruindo forçadamente
# del cachorro
print('a')
print('a')
# Caso não destrua forçadamente, ele destrói a instância no final do código