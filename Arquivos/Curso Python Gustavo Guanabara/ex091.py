from random import randint
from time import sleep
from operator import itemgetter
lugar = 1
jogadores = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)

}
ranking = dict()
print('-----VALORES-----')
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-----RANKING-----')
for k, v in ranking:
    print(f'em {lugar} lugar: {k} com {v} ')
    lugar += 1