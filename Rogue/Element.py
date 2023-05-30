class Element(object):
    """Classe de base pour les éléments du jeu. Avoir un nom.
         Classe abstraite."""

    def __init__(self, name, abbrv=""):
        self.name = name
        if abbrv == "":
            abbrv = name[0]
        self.abbrv = abbrv

    def __repr__(self):
        return self.abbrv

    def description(self):
        """Description de l'element"""
        return "<" + self.name + ">"

    def meet(self, hero):
        """Fait rencontrer un élément par le héros. Non implémenté. """
        raise NotImplementedError('Abstract Element')
