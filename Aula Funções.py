def verificar_par (numero):
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} não é par')
    return

def verifica_vogal (letra):
    vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if letra in vogais:
        print(f'{letra} é uma vogal!')
    else:
        print(f'{letra} é consoante')
    return

# verificar_par (n)
# Verifica se um número é par ou não

# verifica_vogal (letra)
# Verifica se uma letra passada é uma vogal ou não

