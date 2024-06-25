def set ():
    set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

    set('abacaxi') # {'b', 'a', 'c', 'x', 'i'}

    set(('palio', 'gol', 'celta', 'palio')) # {'gol', 'celta', 'palio'}

def acessando_valores_conjuntos ():
    numeros = {1, 2, 3, 4}
    numeros = list(numeros)
    numeros [0] # Não é possível acessar o index de um conjunto

def metodos ():
    # Union
    a = {1, 2}
    b = {3, 4}
    a.union(b) # {1, 2, 3, 4}

    # Intersection
    a = {1, 2, 3}
    b = {2, 3, 4}
    a.intersection(b) # {2, 3}

    # Difference
    a = {1, 2, 3}
    b = {2, 3, 4}
    a.difference(b) # {1}
    b.difference(a) # {4}

    # Symmetric Difference
    a = {1, 2, 3}
    b = {2, 3, 4}
    a.symmetric_difference(b) # {1, 4}

    # Issubset
    a = {1, 2, 3}
    b = {4, 1, 2, 5, 6, 3}
    a.issubset(b) # True
    b.issubset(a) # False

    # Issuperset / Contrário de Issubset
    a = {1, 2, 3}
    b = {4, 1, 2, 5, 6, 3}
    a.issuperset(b) # False
    b.issuperset(a) # True

    # Isdisjoint / Interagem?
    a = {1, 2, 3, 4, 5}
    b = {6, 7, 8, 9}
    c = {1, 0}
    a.isdisjoint(b) # True
    a.isdisjoint(c) # False

    # Add / Caso o elemento não exista, é adicionado
    sorteio = {1, 23}
    sorteio.add(25) # {1, 23, 25}
    sorteio.add(42) # {1, 23, 25, 42}
    sorteio.add(25) # {1, 23, 25, 42}

    # Clear
    sorteio = {1, 23}
    sorteio.clear() # {}

    # Copy
    sorteio = {1, 23}
    sorteio.copy() # {1, 23}

    # Discard / Caso o valor exista, ele descarta
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numeros.discard(1)
    numeros.discard(45)
    print(numeros) # {0, 2, 3, 4, 5, 6, 7, 8, 9}

    # Pop 
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numeros.pop() # 0
    numeros.pop() # 1
    print(numeros) # {2, 3, 4, 5, 6, 7, 8, 9}

    # Remove / Diference do discard, da erro
    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
    print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numeros.remove(0) # 0
    print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    numeros.remove(45) # ERRO

    

