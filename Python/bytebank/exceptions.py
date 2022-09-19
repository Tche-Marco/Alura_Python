class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, message='', saldo=None, valor=None, *args) -> None:
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insificiente para efetuar a transação\n'\
            f'Saldo atual: {self.saldo} Valor a ser sacado {self.valor}'
        self.msg = message or msg
        # self.msg vai tentar receber o retorno da message passada como parametro, caso ela seja False, recebe a variável msg
        super(SaldoInsuficienteError, self).__init__(
            self.msg, self.saldo, self.valor, *args)
