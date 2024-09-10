from typing import Any, Self

class No():

    def __init__(self) -> None:
        self.__dados : Any = None
        self.__prox : No = None
        self.__ant : No = None

    @property
    def prox(self) -> Self:
        return self.__prox
    @prox.setter
    def prox(self, other : Self) -> None:
        self.__prox = other

    @property
    def ant(self) -> Self:
        return self.__ant
    @ant.setter
    def ant(self, other : Self) -> None:
        self.__ant = other

    @property
    def dados(self) -> Any:
        return self.__dados
    @dados.setter
    def dados(self, other : Any) -> None:
        self.__dados = other