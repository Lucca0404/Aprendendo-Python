from collections.abc import Iterator
from typing import Any
from No import No

class Lista():

    def __init__(self) -> None:
        self.__inicio : No = None
        self.__tamanho : int = 0
        self.__index : int = 0

    def __len__(self) -> int:
        return self.__tamanho
    
    def __repr__(self) -> str:
        rep = '['
        no = self.__inicio
        while no is not None:
            rep += str(no.dados) + ','
            no = no.prox
        rep += ']'
        return rep

    def __eq__(self, value: object) -> bool:
        if not isinstance(value,Lista):
            return False
        if self.__tamanho != len(value):
            return False
        no1 = self.__inicio
        no2 = value.__inicio
        while no1 is not None:
            if(no1.dados != no2.dados):
                return False
            no1 = no1.prox
            no2 = no2.prox
        return True
    
    def __iter__(self) -> Iterator:
        self.__index = 0
        return self
    
    def __next__(self) -> Any:
        if self.__index < self.__tamanho:
            no = self.__inicio
            for i in range(self.__index):
                no = no.prox
            self.__index += 1
            return no.dados
        else:
            raise StopIteration
        
    def __lt__(self, value: list) -> bool:
        return self.__tamanho < value.__tamanho
    
    def __gt__(self, value: list) -> bool:
        return self.__tamanho > value.__tamanho
    
    def __str__(self) -> str:
        rep = '['
        no = self.__inicio
        while no is not None:
            rep += str(no.dados) + ','
            no = no.prox
        rep += ']'
        return rep
    
    def __getitem__(self, index):
        no = self.__inicio
        cont = 0
        try:
            while no is not None:
                if cont == index:
                    return no.dados
                no = no.prox
                cont+=1
        except IndexError:
            raise IndexError('Você ultrapassou o índice máximo da lista')

    def ehVazia(self) -> bool:
        return (self.__tamanho == 0)
    
    def pertence(self, dado) -> bool:
        no = self.__inicio
        while no is not None:
            if no.dados == dado:
                return True
            no = no.prox
        return False
    
    def inserirInicio(self, dado) -> None:
        no = No()
        no.prox = self.__inicio
        self.__inicio = no
        no.dados = dado
        self.__tamanho+=1

    def inserirFinal(self, dado) -> None:
        if self.ehVazia():
            self.inserirInicio(dado)
        else:
            no = No()
            aux = self.__inicio
            while aux.prox is not None:
                aux = aux.prox
            aux.prox = no
            no.ant = aux
            no.dados = dado
            self.__tamanho += 1

    def inserirOrdenado(self,dado) -> None:
        if self.ehVazia():
            self.inserirInicio(dado)
        else:
            no = No()
            no.dados = dado
            aux = self.__inicio
            if no.dados < aux.dados:
                self.inserirInicio(dado)
            else:
                while aux.prox is not None and aux.dados < dado:
                    aux = aux.prox
                no.ant = aux
                no.prox = aux.prox
                aux.prox = no
                self.__tamanho += 1

    def removerInicio(self) -> None:
        if self.ehVazia():
            raise PermissionError('A função removerInicio só funcionará caso exista algum elemento dentro da lista')
        no = self.__inicio
        if no.prox is not None:
            no.prox.ant = None
        self.__inicio = no.prox
        self.__tamanho -= 1

    def removerFinal(self) -> None:
        if self.ehVazia():
            raise PermissionError('A função removerFinal só funcionará caso exista algum elemento dentro da lista')
        no = self.__inicio
        if no.prox is None:
            self.__inicio = None
        else:
            while no.prox is not None:
                no = no.prox
            no.ant.prox = None
        self.__tamanho -= 1

    def remover(self, dado) -> None:
        if not self.pertence(dado):
            raise ValueError('O valor inserido no parâmetro "dado" não existe dentro da lista')
        no = self.__inicio
        if no.dados == dado:
            self.removerInicio()
        else:
            while no is not None and no.dados != dado:
                no = no.prox    
            no.ant.prox = no.prox
            self.__tamanho -= 1