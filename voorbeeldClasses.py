# Basic class

class Dier(): # Hoofdletter!
    def __init__(self, naamDier, gewicht, lengte):
        self.naamDier = naamDier
        self.gewicht = gewicht
        self.lengte = lengte
    
    def printGewicht(self): # self is de eerste parameter van elke functie in een klas!!
        print(f'Ik weeg {self.gewicht} kilo')
    
    def berekenBMI(self):
        print(f'Mijn bmi  is {self.gewicht * self.lengte}.')

dier = Dier('olifant', 5000, 3)
# dier2 = Dier('giraf', 2000)

dier.printGewicht()
dier.berekenBMI()