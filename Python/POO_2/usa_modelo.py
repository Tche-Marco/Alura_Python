from modelo import Filme, Serie, Playlist


vingadores = Filme('Vingadores', 2012, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(  # hasattr verifica se um objeto possui certo atributo
        programa, 'duracao') else programa.temporadas  # usando if em apenas uma linha
    print(f'{programa.nome} - {detalhes} - {programa.likes}')

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
