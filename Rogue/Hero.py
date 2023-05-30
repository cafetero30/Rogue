from Creature import Creature
from Equipment import Equipment

class Hero(Creature):
    """Le héros du jeu.
         Est une créature. A un inventaire des éléments. """

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []

    def description(self):
        """Description du héros"""
        return Creature.description(self) + str(self._inventory)

    def fullDescription(self):
        """Description complète du héros"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        """Vérifiez si o est un équipement."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """Le héros prend ajoute l'équipement à son inventaire"""
        self.checkEquipment(elem)
        self._inventory.append(elem)

    def use(self, elem):
        """Utiliser un équipement"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.use(self):
            self._inventory.remove(elem)
