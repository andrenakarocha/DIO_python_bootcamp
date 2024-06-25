# Por padrão, o python não fornece classes abstratas então usamos o módulo ABC
from abc import ABC, abstractmethod

# Criamos uma classe abstrata
class ControleRemoto(ABC):
    # Criamos os métodos abstratos, OBRIGANDO que todas as classes filhas de ControleRemoto, também tenham esse método abstrato
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    # Eu também posso criar propriedades abstratas, OBRIGANDO que todas as classes filhas de ControleRemoto, também tenham essa propriedade abstrata
    @property
    @abstractmethod
    def marca(self):
        pass

# Assim que criamos a classe abstrata, criamos a classe filha com os métodos e propriedades
class ControleTV(ControleRemoto):
    def ligar(self):
        print('TV Ligada')

    def desligar(self):
        print('TV Desligada')

    @property
    def marca(self):
        return 'LG'

# Diferente da herança, quando usadas as classes abstratas, os métodos abstratos PRECISAM ser passados nas classes filhas

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

# Se eu tentar rodar, sem criar todos os métodos ou propriedades feitas na classe abstrata pai, o código crasha. Isso traz uma maior segurança ao código, pois OBRIGA você a criar os métodos.
# Isso também pode ajudar no polimorfismo