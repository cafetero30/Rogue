from Element import Element
import theGame

class Creature(Element):
    """Une créature qui occupe le donjon.
         Est un élément. Possède des points de vie et de la force."""

    def __init__(self, name, hp, abbrv="", strength=1):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength

    def description(self):
        """Description de la creature"""
        return Element.description(self) + "(" + str(self.hp) + ")"

    def meet(self, other):
        """La créature est rencontrée par une autre créature.
             L'autre touche la créature. Renvoie True si la créature est morte."""
        self.hp -= other.strength
        theGame.theGame().addMessage("The " + other.name + " hits the " + self.description())
        if self.hp > 0:
            return False
        return True
