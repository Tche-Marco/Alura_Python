import requests


class BuscaEndereco:

    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!")

    def __str__(self) -> str:
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        return False

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self): 
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
