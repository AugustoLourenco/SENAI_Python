# DESAFIO 03 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.

times = 'Vitória', 'Juventude', 'Criciúma', 'Atlético-GO', 'Novorizontino', 'Mirassol', 'Sport', 'Vila Nova', 'CRB', 'Guarani', 'Ceará', 'Botafogo', 'Avaí', 'Ituano', 'Ponte Preta', 'Chapecoense', 'Sampaio Corrêa', 'Tombense', 'Londrina', 'ABC'

cinco_primerios_colocados = times[:5]
print(cinco_primerios_colocados)

rebaixados = times[-4:]
print(rebaixados)

ordem_alfabetica = sorted(times)
print(ordem_alfabetica)

posicao_santos = times.index('Vitória')
print(posicao_santos+1)