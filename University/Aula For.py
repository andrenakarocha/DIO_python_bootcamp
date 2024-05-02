def comidas_favoritas ():
    comidas = ['feijoada', 'lasanha', 'panqueca', 'miojo', 'pizza', 'strogonoff']
    nomes = ['Danilão', 'Lucas', 'Leandro', 'Wellington', 'Allen', 'Lucas Demetrius']
    for i in range (len(nomes)):
        if nomes[i] == 'Leandro':
            print(f'O {nomes[i]} come {comidas[i]}')

def senha_com_for ():
    for i in range (3):
        tentativa = input('Digite a senha: ')
        if tentativa != '1234':
            print('Senha incorreta!')
            if i < 2:
                print(f'Faltam {2 - i} tentativas!')
        else:
            print('Senha correta!')
    print ('Número de tentativas excedido!')

# comidas_favoritas ()
# Manipulação de 2 arrays para achar a "comida favorita" de cada professor

# senha_com_for ()
# Testa uma senha 3 vezes usando FOR, caso a senha náo seja a certa, pede a senha novamente e printa a quantidade de tentativas restantes
