import re


def cpf_valido(cpf):
    return len(cpf) == 11


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    """ Verifica se o celular é válido (11 98484-8484) """
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    retorno = re.findall(modelo, celular)

    if retorno and len(celular) == 13:
        return retorno
        
    return False
