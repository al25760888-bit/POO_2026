
from Mob import Mob
from Creeper import Creeper
from Enderman import Enderman 
from Vaca import Vaca
from Zombie import Zombie

if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
        Zombie("Zombie",20),
    ]
    for mob in mobs:
        mob.presentarse()
        
        
        