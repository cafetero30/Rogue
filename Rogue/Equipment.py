from Element import Element
import theGame

class Equipment(Element):
    """Une pièce de l'équipement"""

    def __init__(self, name, abbrv="", usage=None):
        Element.__init__(self, name, abbrv)
        self.usage = usage

    def meet(self, hero):
        """Le héros rencontre un élément. Le héros prend l'élément."""
        hero.take(self)
        theGame.theGame().addMessage("You pick up a " + self.name)
        return True

    def use(self, creature):
        """ Utilise la pièce d'équipement. A un effet sur le héros en fonction de son utilisation.
             Renvoie True si l'objet est consommé."""
        if self.usage is None:
            theGame.theGame().addMessage("The " + self.name + " is not usable")
            return False
        else:
            theGame.theGame().addMessage("The " + creature.name + " uses the " + self.name)
            return self.usage(self, creature)
