nametomass = {"H":1.008, "He":4.0026, "Li":6.94, "Be":9.0122, "B":10.81, "C":12.011, "N":14.007, "O":15.999, "F":18.998, "Ne":20.18, "Na":22.990, "Mg":24.305, "Al":26.982, "Si":28.085, "P":30.974, "S":32.06, "Cl":35.45, "Ar":39.948, "K":39.098, "Ca":40.078, "Sc":44.956, "Ti":47.867, "V":50.942, "Cr":51.996, "Mn":54.938, "Fe":55.845, "Co":58.933, "Ni":58.693, "Cu":63.546, "Zn":65.38, "Ga":69.723, "Ge":72.63, "As":74.922, "Se":78.971, "Br":79.904, "Kr":83.798}

class convertclass:
    def __init__(self, element, mass):
        self.element = element
        self.mass = mass

    def convert(self):
        molmass = float(self.mass)/float(nametomass[self.element])
        return "{} grams of {} is equivalent to {} moles.".format(self.mass, self.element, molmass)

def caller():
    print("Symbol of element?")
    elementsymbol = input().title()
    print("Weight of sample of element?")
    elementmass = input()
    testclass = convertclass(elementsymbol, elementmass)
    print(testclass.convert())

while 1==1:
    print("Convert mass of element to moles? y/n")
    answer = input()
    if answer == 'y':
        caller()
    else:
        break

