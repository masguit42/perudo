import random
import time

random.seed(time.time())

class Dice(object):
    """
    No-description
    """
    possible_faces = ("1", "2", "3", "4", "5", "6")

    def __init__(self, face="0"):
        self.face = face

    def toss(self):

        self.face = str(random.choice(self.possible_faces))

    def __str__(self):
        return str(self.face)


class Beaker(object):


    def __init__(self):
        self.NUM_OF_DICES = 5
        self.dices = [Dice() for _ in range(self.NUM_OF_DICES)]

    def shake(self):
        for dice in self.dices:
            dice.toss()
        # self.dices = tuple(map(Dice.toss, self.dices))

    def pop(self):
        self.dices.pop()

    def __str__(self):
        return str(tuple(map(str, self.dices)))


class Player(object):

    def __init__(self, name, id):
        self.beaker = Beaker()
        self.name = name
        self.id = id

    def shake_beaker(self):
        self.beaker.shake()

    def trust_prev(self):
        self.make_move()

    def not_trust_prev(self):
        


# Test
beaker = Beaker()

print(beaker)
for i in range(5):
    beaker.shake()
    if random.getrandbits(1): beaker.pop()
    print(beaker)