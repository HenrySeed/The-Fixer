from engine import *
from level import *
from player import *




engine = Engine()


player = Player(engine)

level1 = Level(player, engine, (100, 100))

bullet = Projectile(player.look_angle, player.pos);
level1.addObject(bullet)

engine.addObject(level1)
engine.addObject(player)




engine.loop()