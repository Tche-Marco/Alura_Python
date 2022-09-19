# verificando sem iterador
registro = open('acessos.log', 'r')
sites_sem_https = [url[:-1] for url in registro if url.startswith('http://')]
print(sites_sem_https)


# verificando com iterador (recomendado)
class IteradorHttp():
    def __init__(self):
        self.registro = open('acessos.log', 'r')
        self.linha_atual = ''

    def __iter__(self):
        return self

    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual[:-1]
        raise StopIteration


iterador = IteradorHttp()
for url in iterador:
    print(url)
