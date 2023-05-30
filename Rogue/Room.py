from Coord import Coord
import Map
import theGame

import random

class Room(object):
    """Une pièce rectangulaire dans le plan"""

    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __repr__(self):
        return "[" + str(self.c1) + ", " + str(self.c2) + "]"

    def __contains__(self, coord):
        return self.c1.x <= coord.x <= self.c2.x and self.c1.y <= coord.y <= self.c2.y

    def intersect(self, other):
        """Tester si la pièce a une intersection avec une autre pièce"""
        sc3 = Coord(self.c2.x, self.c1.y)
        sc4 = Coord(self.c1.x, self.c2.y)
        return self.c1 in other or self.c2 in other or sc3 in other or sc4 in other or other.c1 in self

    def center(self):
        """Renvoie les coordonnées du centre de la pièce"""
        return Coord((self.c1.x + self.c2.x) // 2, (self.c1.y + self.c2.y) // 2)

    def randCoord(self):
        """Une coordonnée aléatoire à l'intérieur de la pièce"""
        return Coord(random.randint(self.c1.x, self.c2.x), random.randint(self.c1.y, self.c2.y))

    def randEmptyCoord(self, map):
        """Une coordonnée aléatoire à l'intérieur de la salle qui est libre sur la carte."""
        c = self.randCoord()
        while map.get(c) != Map.Map.ground or c == self.center():
            c = self.randCoord()
        return c

    def decorate(self, map):
        """Décore la pièce en ajoutant un équipement et un monstre aléatoires."""
        map.put(self.randEmptyCoord(map), theGame.theGame().randEquipment())
        map.put(self.randEmptyCoord(map), theGame.theGame().randMonster())
