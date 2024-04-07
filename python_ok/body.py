print("hello")

class Atom(object):
    def __init__(self, organic):
        self.organic = organic
        print(f"Organic: {organic}")
    def bind(self):
        print("the atom binds with another atom, forming a molecule")

class Molecule:
    def __init__(self, energy, organic):
        self.atom = Atom(organic)
        pass

    def interact(self):
        self.atom.bind()
        print("and the molecules interacted happily ever after")

x = Molecule(True,True)
x.interact()

class Glucose(Molecule):
    def __init__(self, energy, organic):
        super().__init__(energy, organic)

    def run(self):
        print("glucose runs away")

y = Glucose(True,True)
y.run()
y.interact()
