from Element import Element
import theGame

class Stairs(Element):
    """ Escalier qui descend d'un étage. """

    def __init__(self):
        super().__init__("Stairs", 'E')

    def meet(self, hero):
        """Diminue"""
        theGame.theGame().buildFloor()
        theGame.theGame().addMessage("The " + hero.name + " goes down")
