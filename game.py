from engine import *
from level import *
from player import *




engine = Engine()


player = Player(engine)

level1 = Level(player, engine, (100, 100))


engine.level = level1
engine.addObject(player)




engine.loop()
