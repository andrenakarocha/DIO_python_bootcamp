def criando_listas ():

    #lista padrão
    frutas = ['laranja', 'Maçã', 'uva']

    #lista vazia
    frutas = []

    #['p', 'y', 't', 'h', 'o', 'n']
    letras = list('python')

    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numeros = list(range(10))

def index ():
    frutas = ['laranja', 'Maçã', 'uva']
    frutas[0] #laranja
    frutas[2] #uva
    frutas[-1] #uva
    frutas[-3] #laranja

def matrizes ():
    matriz = [
        [1, 'a', 2],
        ['b', 3, 4],
        [6, 5, 'c']
    ]

    matriz[0] # [1, 'a', 3]
    matriz[0][0] # 1
    matriz[0][-1] # 2
    matriz[-1][-1] # 'c'

def fatiamento ():
    lista = ['p', 'y', 't', 'h', 'o', 'n']

    lista [2:] # ['y', 't', 'h', 'o', 'n']
    lista[:2] # ['p', 'y']
    lista[1:3] # ['y', 't']
    lista[0:3:2] # ['p', 't']
    lista[::] # ['p', 'y', 't', 'h', 'o', 'n']
    lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']

def enumerate ():
    carros = ['gol', 'celta', 'palio']

    for i, carro in enumerate(carros):
        print(f'{i}: {carro}')

def one_line ():
    # Código Normal
    numeros = [1, 30, 21, 2, 9, 64, 33]
    pares = []
    
    for i in range (len(numeros)):
        if numeros[i] % 2 == 0:
            pares.append(numeros[i]) 
    print(pares)

    # One line
    numeros = [1, 30, 21, 2, 9, 64, 33]
    pares = [numeros[i] for i in range(len(numeros)) if numeros[i] % 2 == 0]
    print(pares)

    # Outro exemplo
    numeros = [1, 30, 21, 2, 9, 64, 33]
    quadrados = [numeros[i] ** 2 for i in range(len(numeros))]
    print(quadrados)

def list_methods ():
    # Append
    lista = []
    lista.append(1)
    lista.append('Python')
    lista.append([40, 30, 20])
    print(lista) # [1, 'Python', [40, 30, 20]]

    # Clear
    lista2 = [1, 2, 3, 4]
    lista2.clear()
    print(lista2) # []

    # Copy
    lista3 = [1, 2, 3, 4]
    l2 = lista3.copy
    print(id(l2), id(lista3)) # copia a lista, guardando em outra variável

    # Count
    lista4 = [1, 2, 2, 4]
    lista4.count(1) # 1 
    lista4.count(2) # 2

    # Extend
    linguagens = ['python', 'js', 'C']
    linguagens.extend(['java', 'C#'])
    print(linguagens) # ['python', 'js', 'C', 'java', 'C#']

    # Index
    linguagens.index('java') # 3
    linguagens.index('python') # 0 

    # Pop
    linguagens.pop() # C#
    linguagens.pop() # java
    linguagens.pop() # C
    linguagens.pop(0) # python

    # Remove
    linguagens.remove('C') # Remove o objeto 'C'
    # Se houver mais de um elemento igual, remove apenas o primeiro encontrado

    # Reverse
    linguagens.reverse() # ['C#', 'java', 'C', 'js', 'python']

    # Sort
    linguagens.sort() # Ordena alfabeticamente
    linguagens.sort(reverse=True) # Ordena alfabeticamente e inverte ela
    linguagens.sort(key=lambda x: len(x)) # Ordena em ordem crescente de caracteres
    linguagens.sort(key=lambda x: len(x), reverse=True) # Ordena em ordem crescente de caracteres e inverte ela

    # Len
    len(linguagens) # 5

    # Sorted
    sorted(linguagens, key=lambda x: len(x)) # Mesma coisa que o sort(), porém em uma função