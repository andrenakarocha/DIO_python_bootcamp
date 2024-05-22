def criando_dicionarios ():
    pessoa = {'nome': 'Guilherme', 'idade': 28}

    # Usando dict
    pessoa = dict(nome = 'Guilherme', idade = 28)

    # Atribuindo valores
    pessoa['telef1one'] = '9999-1234'

def acessando_dados ():
    dados = {'nome': 'Guilherme', 'idade': 28, 'telefone': '9999-1234'}

    dados['nome'] # 'Guilherme'
    dados['idade'] # 28
    dados['telefone'] # '9999-1234'

    # Sobrescrevendo valores
    dados['nome'] = 'Maria'
    dados['idade'] = 18
    dados['telefone'] = '3333-1234'

    print(dados) # {'nome': 'Maria', 'idade': 18, 'telefone': '3333-1234'}

def exemplo_de_uso ():
    contatos = {
        'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
        'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
        'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
    }

    print(contatos['guilherme@gmail.com']['idade']) # 28

def metodos_dicionario ():

    def clear ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
            'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
            'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
        }
            
        contatos.clear()
        print(contatos) # {}

    def copy ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
            'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
            'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
        }

        # Copia os dados para outro dicionario
        copia = contatos.copy()

        copia['guilherme@gmail.com'] = {'nome': 'Gui'}

        contatos['guilherme@gmail.com'] # {'nome': 'Guilherme', 'idade': 28}
        copia['guilherme@gmail.com'] # {'nome': 'Gui', 'idade': 28}

    def fromkeys ():
        dict.fromkeys(['nome', 'telefone']) # {'nome': None, 'telefone': None}
        
        dict.fromkeys(['nome', 'telefone'], 'valor_padrao') # {'nome': valor_padrao, 'telefone': valor_padrao}

    def get ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        # Faz o codigo parar
        contatos['chave'] # KeyError

        # O codigo nao para
        contatos.get('chave') # None

        # Caso nao encontre, retorna um dicionario vazio
        contatos.get('chave', {}) # {}

        contatos.get('guilherme@gmail.com', {}) # {'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}}

    def items ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        contatos.items() # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'idade': 28})])

    def keys ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        contatos.keys() # dict_keys(['guilherme@gmail.com'])
    
    def pop ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        contatos.pop('guilherme@gmail.com') # {'nome': 'Guilherme', 'idade': 28}

        # Caso nao encontre, retorna valor padrao
        contatos.pop('guilherme@gmail.com', {}) # {}

    def popitem ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        contatos.popitem() # ('guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28})

        # Nao pode passar valor padrao
        contatos.popitem() # KeyError

    def setdefault ():
        dados = {'nome': 'Guilherme', 'idade': 28, 'telefone': '9999-1234'}

        # Como ja existe, nao altera
        dados.setdefault('nome', 'Giovana') # 'Guilherme
        print(dados) # {'nome': 'Guilherme', 'idade': 28, 'telefone': '9999-1234'}

        # Como nao existe, adiciona o valor
        dados.setdefault('genero', 'masculino')
        print(dados) # {'nome': 'Guilherme', 'idade': 28, 'telefone': '9999-1234', 'genero': 'masculino'}

    def update ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28}
        }

        # Update com uma chava existente, muda o valor
        contatos.update({'guilherme@gmail.com': {'nome': 'Gui'}})
        print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}}

        # Update com uma chave nao existente, adiciona os valores no dict
        contatos.update({'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39}})
        print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39}

    def values():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
            'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
            'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
        }

        print(contatos.values()) # dict_values([{'nome': 'Guilherme', 'idade': 28}, {'nome': 'Giovana', 'idade': 39}, {'nome': 'Melaine', 'idade': 15}])

    def in_ ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
            'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
            'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
        }

        print('guilherme@gmail.com' in contatos) # True

        print('megu@gmail.com' in contatos) # False

        print('telefone' in contatos['guilherme@gmail.com']) # False

        print('idade' in contatos['giovana@gmail.com']) # True

    def del_ ():
        contatos = {
            'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28},
            'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39},
            'melaine@gmail.com': {'nome': 'Melaine', 'idade': 15},
        }

        del contatos['guilherme@gmail.com']['idade']
        del contatos['melaine@gmail.com']

        print(contatos) # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovana@gmail.com': {'nome': 'Giovana', 'idade': 39}}