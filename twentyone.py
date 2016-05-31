import random
_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def _carta_siguiente():
    return random.choice(_cartas)


class Crupier():
    def __init__(self):
        self.mano = []

    def nueva_ronda(self):
        self.mano = [_carta_siguiente(), _carta_siguiente()]
