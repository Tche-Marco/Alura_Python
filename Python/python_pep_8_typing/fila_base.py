import abc  # Abstract Base Classes
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):  # declara classe como abstrata

    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo > TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod  # declara o método como abstrato
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractmethod  # declara o método como abstrato
    def chama_cliente(self, caixa: int):
        ...
