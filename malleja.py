import random, math
from random import random

# value importante
birthRate = 40.87/1000
deathRate = 13.91/1000


#Luokat
class Ihminen:
    """Jokaisen ihmisen pohja"""

    def __init__(self):
        self.exposed = False
        self.Peelo = True
        self.Immune= False
        # 1 = child/young, 2 = adult and 3 = possible middle-aged
        self.age = random.choose([1,2,3])
        # Ihmisen sukupuoli. Koska nainen on aina oikeassa nainen = True
        self.gender = random() >= 0.5

    def kantajanMuutos(self, boolean):
        self.exposed = boolean

    def immuuniMuutos(self, boolean):
        self.Immune = boolean

class village:
    """Container of humans"""

    def __init__(self, humans):
        self.villageHumans = humans
        self.population = size(humans)

    def vuosiVaihtuu(self):
        for i in range(birthRate * self.määrä):
            villageHumans.add(Ihminen())
            self.määrä += 1
        
