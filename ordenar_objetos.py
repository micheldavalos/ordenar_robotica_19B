from random import randint
class Automovil:
    def __init__(self):
        self.placas = ""
        self.modelo = 0
        self.marca = ""
        self.km = 0

    def __str__(self):
        return "{0:7}  {1:4} {2:6} {3:4}".format(self.placas, self.modelo, self.marca, self.km)

    def __lt__(self, other):
        return self.modelo < other.modelo

marcas = ["VM", "Audi", "BMW", "Fiat", "Nissan"]
placas = ["ABC", "JVC", "JZM", "MDB", "UDG"]

autos = []

for i in range(0, 100):
    a = Automovil()
    a.placas = placas[randint(0, 4)] + "-" + str(randint(100, 999))
    a.marca = marcas[randint(0, 4)]
    a.modelo = randint(2000, 2019)
    a.km = randint(0, 1000)

    autos.append(a)

# autos.sort()
def sort_by_km(auto):
    return auto.km

# autos.sort(key=sort_by_km, reverse=True)
# autos.sort(key=lambda auto: auto.marca)
autos.sort(key=lambda auto: auto.placas)
for auto in autos:
    print(auto)




