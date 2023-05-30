import theGame

def heal(creature):
    """Soigner la créature"""
    creature.hp += 3
    return True

def teleport(creature, unique):
    """Téléporter la créature"""
    r = theGame.theGame()._floor.randRoom()
    c = r.randEmptyCoord(theGame.theGame()._floor)
    theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(creature))
    theGame.theGame()._floor.put(c, creature)
    return unique

def throw(power, loss):
    """Lancer un objet"""
    pass
