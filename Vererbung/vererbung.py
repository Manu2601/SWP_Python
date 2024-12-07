class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"Das {self.name} wird gespielt.")


class StringInstrument(Instrument):
    def __init__(self, name, strings):
        super().__init__(name)
        self.strings = strings

    def tune(self):
        print(f"Das {self.name} mit {self.strings} Saiten wird gestimmt.")


class WindInstrument(Instrument):
    def __init__(self, name, body_material):
        super().__init__(name)
        self.body_material = body_material

    def clean(self):
        print(f"Das {self.name}, aus {self.body_material} gefertigt, wird gereinigt.")


class Guitar(StringInstrument):
    def __init__(self, name, strings=6):
        super().__init__(name, strings)

    def play(self):
        print(f"Das {self.name} mit {self.strings} Saiten wird gespielt.")


class Violin(StringInstrument):
    def __init__(self, name, strings=4, bow_length=75):
        super().__init__(name, strings)
        self.bow_length = bow_length

    def play(self):
        print(f"Die {self.name} wird mit einem {self.bow_length} cm langen Bogen gespielt.")


class Clarinet(WindInstrument):
    def __init__(self, name, reed_type, body_material="Holz"):
        super().__init__(name, body_material)
        self.reed_type = reed_type

    def play(self):
        print(f"Die {self.name} wird mit einem {self.reed_type}-Blatt gespielt, gefertigt aus {self.body_material}.")


class Trumpet(WindInstrument):
    def __init__(self, name, valves=3, body_material="Messing"):
        super().__init__(name, body_material)
        self.valves = valves

    def play(self):
        print(f"Die {self.name} mit {self.valves} Ventilen aus {self.body_material} wird gespielt.")

    def adjust_valves(self):
        print(f"Die {self.valves} Ventile der {self.name} werden eingestellt.")


class HybridInstrument(StringInstrument, WindInstrument):
    def __init__(self, name, strings, body_material):
        self.name = name 
        self.strings = strings 
        self.body_material = body_material 
    
    def play(self):
        print(f"Das Hybrid-Instrument {self.name} wird sowohl als Saiteninstrument als auch als Blasinstrument gespielt.")

    def tune_and_clean(self):
        self.tune()
        self.clean()



guitar = Guitar("Akustikgitarre", strings=12)
violin = Violin("Geige", bow_length=70)
clarinet = Clarinet("Klarinette", reed_type="einfach", body_material="Ebenholz")
trumpet = Trumpet("Trompete", valves=4, body_material="vergoldetes Messing")

guitar.play()
guitar.tune()

violin.play()
violin.tune()

clarinet.play()
clarinet.clean()

trumpet.play()
trumpet.adjust_valves()

hybrid = HybridInstrument("Hybrid-Instrument", strings=6, body_material="Holz")
hybrid.play()
hybrid.tune_and_clean()

