import sys
class Zimmer():
    def __init__(self, zimmerNr, isBesetzt):
        self.zimmerNr = zimmerNr
        self.isBesetzt = isBesetzt
    
    def __str__(self):
        return "ZimmerNr: {} istBesetzt: {}".format(self.zimmerNr, self.isBesetzt)
    
class Einzelzimmer(Zimmer):
        def __init__(self, zimmerNr, isBesetzt, preis):
            super().__init__(zimmerNr, isBesetzt)
            self.preis = preis
            
class Doppelzimmer(Zimmer):
        def __init__(self, zimmerNr, isBesetzt, preis):
            super().__init__(zimmerNr, isBesetzt)
            self.preis = preis
            
class Hotel():
    def __init__(self, name):
        self.name = name
        self.zimmer = []
        
    def amountFreeRooms(self):
        return len([z for z in self.zimmer if not z.isBesetzt])
    
    def bookRoomWithNr(self, zimmerNr):
        for z in self.zimmer:
            if z.zimmerNr == zimmerNr:
                z.isBesetzt = True
                print("ZimmerNr: {} wurde gebucht.".format(z.zimmerNr))
                return z
            else:
                print("ZimmerNr nicht gefunden.")
        return None
    
    def bookRoom(self, size):
        for z in self.zimmer:
            if not z.isBesetzt and isinstance(z, size):
                z.isBesetzt = True
                print("ZimmerNr: {} wurde gebucht.".format(z.zimmerNr))
                return z
        return None
    
    def cancelBooking(self, zimmerNr):
        for z in self.zimmer:
            if z.zimmerNr == zimmerNr:
                z.isBesetzt = False
                print("ZimmerNr: {} wurde storniert.".format(z.zimmerNr))
                return z
        return None
    
def main():
    h = Hotel("Meininger")
    h.zimmer.append(Einzelzimmer(1, False, 100))
    h.zimmer.append(Doppelzimmer(2, False, 200))
    h.zimmer.append(Einzelzimmer(3, False, 100))
    h.zimmer.append(Doppelzimmer(4, False, 200))
    
    print(h.amountFreeRooms())
    
    h.bookRoomWithNr(1)
    print(h.amountFreeRooms())
    
    h.bookRoomWithNr(2)
    print(h.amountFreeRooms())
    
    h.cancelBooking(1)
    print(h.amountFreeRooms())
    
    h.bookRoom(Einzelzimmer)
    print(h.amountFreeRooms())
    
    h.bookRoom(Doppelzimmer)
    print(h.amountFreeRooms())
    
if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
    