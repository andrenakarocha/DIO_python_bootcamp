def passando_parametros ():

    def salvar_carro(marca, modelo, ano, placa):
        print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
        
    # Padrao
    salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')

    # Mais especifica (Independente da ordem)
    salvar_carro(marca = 'Fiat', modelo = 'Palio', ano = 1999, placa = 'ABC-1234')

    # Usando dicionarios (Nao muito usado)
    salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234'})

def positional_only ():

    def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
        print(modelo, ano, placa, marca, motor, combustivel)

    # Todos os parametros antes da barra devem ser apenas posicionais, sem KEYWORDS (Depois da barra, sao sua escolha)
    criar_carro('Palio', 1999, 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # valido

    criar_carro(modelo = 'Palio', ano = 1999, placa = 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # invalido

def keyword_only ():

    def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
        print(modelo, ano, placa, marca, motor, combustivel)

    criar_carro(modelo = 'Palio', ano = 1999, placa = 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # valido

    criar_carro('Palio', 1999, 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # invalido

def keyword_and_positional_only ():

    def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
        print(modelo, ano, placa, marca, motor, combustivel)

    criar_carro('Palio', 1999, 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # valido

    criar_carro(modelo = 'Palio', ano = 1999, placa = 'ABC-1234', marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina') # invalido

