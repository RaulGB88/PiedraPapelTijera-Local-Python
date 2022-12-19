import random


NAME = 'Dime tu nombre por favor: '
PLAY = 'Indica qué quieres jugar: '
ERROR = 'Error. Se ha producido un error insesperado.'

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'
NOT_GAME = 'Error, introduce un juego válido.'

WINNER = 'Gana: '
SAME = 'Empate.'
MACHINE = 'la máquina.'

ERROR = 'ERROR'


def playerGame(game):

    game = game.lower()
    
    while game != PIEDRA or game != PAPEL or game != TIJERA:
        if game == PIEDRA:
            return game
        elif game == PAPEL:
            return game
        elif game == TIJERA:
            return game
        else:
            game = input(PLAY)


def randomGame():
    pos = random.randrange(3)
    game = PIEDRA

    if pos == 0:
        game = PIEDRA
    elif pos == 1:
        game = PAPEL
    elif pos == 2:
        game = TIJERA
    else:
        print(ERROR)

    return game


def executePlay(player, play_one, play_two):

    # PIEDRA
    if play_one == PIEDRA and play_two == PIEDRA:
        result = SAME
    elif play_one == PIEDRA and play_two == PAPEL:
        result = WINNER + MACHINE
    elif play_one == PIEDRA and play_two == TIJERA:
        result = WINNER + player
    # PAPEL
    if play_one == PAPEL and play_two == PIEDRA:
        result = WINNER + player
    elif play_one == PAPEL and play_two == PAPEL:
        result = SAME
    elif play_one == PAPEL and play_two == TIJERA:
        result = WINNER + MACHINE
    # TIJERA
    if play_one == TIJERA and play_two == PIEDRA:
        result = WINNER + MACHINE
    elif play_one == TIJERA and play_two == PAPEL:
        result = WINNER + player
    elif play_one == TIJERA and play_two == TIJERA:
        result = SAME

    return result
    

def init():
    name = input(NAME)
    print('Hola ' + name)

    play = input(PLAY)

    play = playerGame(play)

    randomPlay = randomGame()

    winner = executePlay(name, play, randomPlay)
    print(winner)

if __name__ == '__main__':
    init()
