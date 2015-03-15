import random, math
from random import random

# Tärkeät luvut
birthRate = 40.87/1000
deathRate = 13.91/1000


#Luokat
class Ihminen:
    """Jokaisen ihmisen pohja"""

    def __init__(self):
        self.kantaja = False
        self.Peelo = True
        self.Immuuni = False
        # 1 = lapsi/nuori, 2 = aikuinen ja 3 = mahdollinen keski-ikäinen
        self.ikä = random.choose([1,2,3])
        # Ihmisen sukupuoli. Koska nainen on aina oikeassa nainen = True
        self.sukupuoli = random() >= 0.5

    def kantajanMuutos(self, boolean):
        self.kantaja = boolean

    def immuuniMuutos(self, boolean):
        self.Immuuni = boolean

class kylä:
    """Container of humans"""

    def __init__(self, ihmiset):
        self.kylänIhmiset = ihmiset
        self.määrä = size(ihmiset)

    def vuosiVaihtuu(self):
        for i in range(birthRate * self.määrä):
            kylänIhmiset.add(Ihminen())
            self.määrä += 1
        
