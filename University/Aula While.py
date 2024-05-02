#Pares e Ímpares (While)
def pares_e_impares () :
    repeticoes = 0
    pares = 0
    while repeticoes < 5:
        num = int(input('Diga um número: '))
        if num%2==0:
            pares += 1
        repeticoes += 1
    impares = 5 - pares
    print(f'O número de pares foi {pares} e o número de ímpares foi {impares}')

#Testando senha com While
def teste_de_senha () :
    senha = input('Digite a senha: ')
    while senha != '1234':
        print ('Senha incorreta!')
        senha = input('Digite a senha: ')
    print('Senha correta!')

#Bloqueando o acesso com 3 senhas incorretas
def senha_acesso_bloqueado () :
    senha = input('Digite a senha: ')
    tentativas = 1
    while senha != '1234' and tentativas < 3:
        print (f'Senha incorreta! Você tem mais {3-tentativas} tentativas!')
        senha = input('Digite a senha: ')
        tentativas += 1
    if senha == '1234':
        print('Senha correta!')
    else:
        print('Acesso Negado!')

#Soma de 10 números pedidos com while
def soma_10_numeros () :
    quant_num = 0
    soma = 0
    while quant_num < 10:
        num = int(input('Digite um número: '))
        quant_num += 1
        soma += num
    print(f'A soma de todos os números é {soma}')

#Soma de 10 até 1 com while
def soma_10_ate_1 () :
    i = 11
    soma = 0
    while i > 0:
        i -= 1
        soma += i
        print(soma)

#Frase com 10 palavras com while
def frase_10_palavras () :
    i = 0
    frase = ''
    while i < 10:
        pal = input('Digite uma palavra: ')
        i += 1
        frase += ' ' + pal
        print(frase)

#Quantidade de vogais e consoantes
def contar_vogais_consoantes () :
    i = 0
    vogais = 0
    consoantes = 0
    while i < 10:
        letra = input('Digite uma letra: ')
        i += 1
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1
        else:
            consoantes += 1
    print(f"A quantidade de vogais é {vogais} e a quantidade de consoantes é {consoantes}")

#Verificar e transformar um número inteiro
def tratamento_de_numero () :
    n = input('Digite um número: ')
    while not n.isnumeric():
        print('Isso não é um número!')
        n = input('Digite um número: ')
    print('É numero')
    n = int(n)

#EXERCÍCIO 1
def exercicio1 () :
    nota = int(input("Digite uma nota entre 0 e 10: "))
    while nota > 10 and nota > 0:
        print('Valor incorreto!')
        nota = int(input("Digite uma nota entre 0 e 10: "))
    print('Valor correto')

#EXERCÍCIO 2
def exercicio2 () :
    nome = str(input('Digite seu nome: '))
    while len(nome) < 3:
        print('Nome inválido')
        nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    while not (0 < idade <= 150):
        print('Idade inválida')
        idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    while salario < 0:
        print('Salário inválido')
        salario = float(input('Digite seu salário: '))
    sexo = str(input('Digite seu sexo (M ou F): '))
    while sexo != 'F' and sexo != 'M':
        print('Sexo inválido')
        sexo = str(input('Digite seu sexo (M ou F): '))
    est_cv = str(input('Digite o seu estado civil (S, C, V ou D)'))
    while est_cv != 'S' and est_cv != 'C' and est_cv != 'V' and est_cv != 'D':
        print('Estado Civil Inválido!')
        est_cv = str(input('Digite o seu estado civil (S, C, V ou D)'))

#EXERCÍCIO 3
def exercicio3 () :
    populacao_pais_A = 80000
    populacao_pais_B = 200000
    anos = 0
    while populacao_pais_A < populacao_pais_B:
        populacao_pais_A *= 0.03
        populacao_pais_B *= 0.015
        anos += 1
    print(f'Demorou {anos} anos.')

#EXERCÍCIO 4
def exercicio4 () :
    i = 0
    soma = 0
    while i < 5:
        n = int(input('Digite um número: '))
        soma += n
        i += 1
    print(f'A soma dos números é {soma} e a média entre eles é {soma/i}')

#EXERCÍCIOS 5
def exercicio5 () :
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    if n1 > n2:
        vn2 = n2
        n2 = n1
        n1 = vn2
    i = n1
    while i < n2:
        i += 1
        print(i)

#EXERCÍCIO 6
def exercicio6 ():
    usuario = input('Digite o seu nome de usuário: ')
    senha = input('Digite a sua senha: ')
    while usuario == senha:
        print('O nome de usuário não pode ser o mesmo que a sua senha!')
        usuario = input('Digite o seu nome de usuário: ')
        senha = input('Digite a sua senha: ')
    print('Cadastro registrado!')

#EXERCÍCIO 7
def exercicio7 () :
    tabuada = int(input('Digite o número da tabuada a ser gerada: '))
    print(f'Tabuada do {tabuada}')
    i = 1
    while i < 11:
        print(f'{tabuada} x {i} = {tabuada*i}')
        i += 1

#PRINTAR TODAS AS TABUADAS
def exercicio7_printar_todas_tabuadas () :
    tabuada = 1
    while tabuada <= 10:
        print(f'Tabuada do {tabuada}')
        i = 1
        while i <= 10:
            print(f'{tabuada} x {i} = {tabuada*i}')
            i += 1
        tabuada += 1

#EXERCÍCIO 8
def exercicio8 () :
    n = int(input('Digite o termo a terminar a sequência de Fibonacci: '))
    i = 1
    n1 = 1
    n2 = 1
    print('1 \n1')
    while i < n:
        i += 1
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n1 + n2)

#EXERCÍCIO 9
def exercicio9 () :
    repeticoes = 0
    pares = 0
    while repeticoes < 10:
        num = int(input('Diga um número: '))
        if (num % 2) == 0:
            pares += 1
        repeticoes += 1
    impares = 10 - pares
    print(f'O número de pares foi {pares} e o número de ímpares foi {impares}')

#EXERCÍCIO 10
def exercicio10 () :
    n = int(input('Digite um número para saber seu fatorial: '))
    fatorial = n
    fatorial_string = str(f"{n}")
    while 1 < n:
        n -= 1
        fatorial *= n
        fatorial_string += f"*{n}"
    print(f'{fatorial_string} = {fatorial}')

#EXERCÍCIO 11
def exercicio11 () :
    n = int(input('Digite um número: '))
    i = 2
    while i < n:
        primo = n % i
        i += 1
        if primo == 0:
            resultado = 'não é primo'
            break
        elif primo != 0:
            resultado = 'é primo'
    print(f'Esse número {resultado}')

#EXERCÍCIO 11 MELHORADO
def exercicio11_melhorado () :
    n = int(input('Digite um número: '))
    i = 2
    if n == 2 or n == 1:
        resultado = 'é primo'
    while True:
        if n % i == 0:
            resultado = 'não é primo'
            break
        elif i >= n ** 0.5:
            resultado = 'é primo'
            break
        i += 1
    print(f'Esse número {resultado}')


#EXERCÍCIO 12
def exercicio12 () :
    quantidade_notas = float(input('Digite a quantidade de notas desejadas para calcular sua média: '))
    while not quantidade_notas.isnumeric():
        print ("Isso não é uma nota válida!")
        quantidade_notas = float(input('Digite a quantidade de notas desejadas para calcular sua média: '))        
    quantidade_notas = int(quantidade_notas)
    i = 0
    soma = 0
    while i < quantidade_notas:
        notas = float(input(f'Digite a {i + 1}º nota: '))
        while not notas.isnumeric():
            print("Nota inválida, digite um número!")
            continue
        notas = float(notas)
        soma += notas
        i += 1
    print(f'A média das suas notas foi: {soma/quantidade_notas:.2f}')

#EXERCÍCIO 13
def exercicio13 () :
    salario_inicial = float(input('Digite o salário inicial: '))
    aumento = 0.015
    salario = salario_inicial + (salario_inicial * aumento)
    ano = 1997
    while ano < 2000:
        aumento *= 2
        ano += 1
        salario += salario * aumento
        print(f'No ano {ano} o aumento foi de {aumento} e o salário foi {salario:.2f}')

#EXERCÍCIO 14
def exercicio14 () :
    intervalo25 = 0
    intervalo50 = 0
    intervalo75 = 0
    intervalo100 = 0
    while True:
        numero = input('Digite um número positivo entre 1 - 100 (Para sair, digite um número negativo): ')
        if '-' in numero:
            print(f'Segue abaixo a quantidade de números em cada seguinte intervalo:' 
                f'\n[0-25]: {intervalo25}'
                f'\n[26-50]: {intervalo50}'
                f'\n[51-75]: {intervalo75}'
                f'\n[76-100]: {intervalo100}')
            break
        if not numero.isnumeric():
            print("Inválido! Digite um número!")
            continue
        numero = float(numero)
        if numero <= 25:
            intervalo25 += 1
        elif numero <= 50:
            intervalo50 += 1 
        elif numero <= 75:
            intervalo75 += 1
        elif numero <= 100:
            intervalo100 += 1
        else:
            print('Número grande demais!')

#EXERCÍCIO 15
def exercicio15 () :
    print('---ELEIÇÕES FODAS---\nSegue abaixo os canditados: '
        '\n1 - José'
        '\n2 - João'
        '\n3 - Carla'
        '\n4 - Paulo'
        '\n5 - Voto Nulo'
        '\n6 - Voto em Branco')
    votos_jose = 0
    votos_joao = 0
    votos_carla = 0
    votos_paulo = 0
    votos_nulo = 0
    votos_branco = 0
    voto = 0
    while voto < 20:
        voto_escolhido = int(input('Digite o número do respectivo candidato escolhido: '))
        if voto_escolhido == 1:
            votos_jose +=1
        elif voto_escolhido == 2:
            votos_joao +=1
        elif voto_escolhido == 3:
            votos_carla += 1
        elif voto_escolhido == 4:
            votos_paulo += 1
        elif voto_escolhido == 5:
            votos_nulo += 1
        elif voto_escolhido == 6:
            votos_branco += 1
        else:
            print('Voto inválido!')
            continue
        voto += 1
    total_votos = votos_joao + votos_jose + votos_carla + votos_paulo
    porcentagem_nulo = votos_nulo / total_votos
    porcentagem_branco = votos_branco / total_votos
    print(f'Segue os dados:'
        f'\nA quantidade de votos para José foi {votos_jose}'
        f'\nA quantidade de votos para João foi {votos_joao}'
        f'\nA quantidade de votos para Carla foi {votos_carla}'
        f'\nA quantidade de votos para Paulo foi {votos_paulo}'
        f'\nA quantidade de votos Nulo foi {votos_nulo}'
        f'\nA quantidade de votos em Branco foi {votos_branco}'
        f'\nO total de votos foi {total_votos}'
        f'\nA porcentagem de votos Nulo sobre o total de votos foi {porcentagem_nulo:.2f}'
        f'\nA porcentagem de votos em Branco sobre o total de votos foi {porcentagem_branco:.2f}')
    
def exercicio15_array ():
    votos_possiveis = ['1', '2', '3', '4', '5', '6']
    votos_jose = 0
    votos_joao = 0
    votos_joaquim = 0
    votos_jorel = 0
    votos_nulo = 0
    votos_branco = 0
    i = 0
    while i < 10:
        voto = input('Diga seu voto: \n1- José\n2 - João\n3- Joaquim\n4 - Jorel\n5 - Nulo\n6 - Branco\n->')
        while voto not in votos_possiveis:
            print('Digite um voto válido!!')
            voto = input('Diga seu voto: \n1- José\n2 - João\n3- Joaquim\n4 - Jorel\n5 - Nulo\n6 - Branco')
        if voto == '1':
            votos_jose += 1
        elif voto == '2':
            votos_joao += 1
        elif voto == '3':
            votos_joaquim += 1
        elif voto == '4':
            votos_jorel += 1
        elif voto == '5':
            votos_nulo += 1
        else:
            votos_branco += 1
        i += 1
    print (f'O José recebeu {votos_jose} votos\n'
           f'O João recebeu {votos_joao} votos\n'
           f'O Joaquim recebeu {votos_joaquim} votos\n'
           f'O Jorel recebeu {votos_jorel} votos\n'
           f'{votos_branco} pessoas ({votos_branco / i:.2f}%) votaram em Branco\n'
           f'{votos_nulo} ({votos_nulo / i:.2f}%) pessoas votaram em Nulo')


# pares_e_impares ()
# Acha a quantidade de pares e ímpares conforme os inputs que o usuário deu

# teste_de_senha ()
# Teste de senha básico

# senha_acesso_bloqueado ()
# Mesmo código acima, porém, bloqueia o acesso caso ultrapasse 3 tentativas

# soma_10_numeros ()
# Soma de 10 números que o usuário forneceu
    
# soma_10_ate_1 ()
# Soma dos números 10 até 1, ou seja, 10+9+8...
    
# frase_10_palavras ()
# Somando palavras que pedidos ao usuário usando strings

# contar_vogais_consoantes ()
# Conta a quantidade de vogais e consoantes que o usuário forneceu
    
# tratamento_de_numero ()
# Entende quando um input é um número ou não, avisando o usuário quando não é um número
    
# exercicio1 ()
# Identificando se uma nota está entre 0 e 10, tratamento de código

# exercicio2 ()
# Várias verificações, treinando tratamento de código
    
# exercicio3 ()
# Mostrar quantos anos demorou para a população de um país ultrapassar a do outro com certas condições

# exercicio4 ()
# Mostrar a soma e média de 5 números

# exercicio5 ()
# Digitar dois números e indicar o maior
    
# exercicio6 ()
# Verificar se o nome de usuário é o mesmo que a senha, caso for, não permitir o cadastro
    
# exercicio7 ()
# Gerar uma tabuada do número que o usuário forneceu
    
# exercicio7_printar_todas_tabuadas ()
# Printar todas as tabuadas do 1 até 10

# exercicio8 ()
# Sequência de Fibonnaci pedindo para o usuário até qual termo ele desejar saber
    
# exercicio9 ()
# Contar a quantidade de pares e ímpares 
    
# exercicio10 ()
# Calcular o fatorial de um respectivo número
    
# exercicio11 ()
# Identificar se um número é ou não primo
    
# exercicio11_melhorado ()
# Verificar um número primo, mas melhorado para verificar menos números (Contas malucas do Danilão)
    
# exercicio12 ()
# Calculando a média de um aluno e tratando o código conforme o necessário
    
# exercicio13 ()
# Salário de um funcionario se seu aumento dobrasse a cada ano

# exercicio14 ()
# Identificar números em seus respectivos intervalos

#exercicio15 ()
# Simulação de eleiçoes contabiliza a quantidade de votos e mostra as porcentagens  

# exercicio15_array ()
# Exercício 15, porém, utilizando arrays para verificar
