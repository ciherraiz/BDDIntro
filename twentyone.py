import random
_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def _carta_siguiente():
    return random.choice(_cartas)


def _total_mano (mano):
    valores = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    mapeo_valores = {k: v for k, v in zip(_cartas, valores)}

    total = sum([mapeo_valores[carta] for carta in mano if carta != 'A'])
    cuenta_ases = mano.count('A')

    for i in range(cuenta_ases, -1, -1):
        if i == 0:
            total = total + cuenta_ases
        elif total + (i * 11) + (cuenta_ases - i) <= 21:
            total = total + (i * 11) + cuenta_ases - i
            break

    return total


class Crupier():
    def __init__(self):
        self.mano = []

    def nueva_ronda(self):
        self.mano = [_carta_siguiente(), _carta_siguiente()]

    def total_mano(self):
        return _total_mano(self.mano)
