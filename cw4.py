# Ćwiczenie 1. Napisz klasę Trip z atrybutami destination oraz price.
# Stwórz w niej inicjalizator w dwoma argumentami.
#

class Trip:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    def show_price(self):
        print(f' Price: {self.price}')
trip = Trip(2,3)
trip.show_price()


# Ćwiczenia 2. 1. Napisz klasę Product. Klasa powinna posiadać atrybuty :
#
#     name typu str (pol. nazwa)
#     price typu float (pol. cena)
#     quality typu int (pol. jakość)
#     tax typu float (pol. podatek)
