class Animals:
    def __init__(self, height, weight, animaltype, bloodtype):
        self.height = height
        self.weight = weight
        self.animaltype = animaltype
        self.bloodtype = bloodtype

    def printanimal(self):
        print(self.height, self.weight, self.animaltype, self.bloodtype)


class Reptile(Animals):
    def __init__(self, height, weight, animaltype, bloodtype, Dryskin, backbone, softshelledeggs, info):
        super().__init__(height, weight, animaltype, bloodtype)
        self.Dryskin = Dryskin
        self.backbone = backbone
        self.softshelled = softshelledeggs
        self.info = Animals

    def showinfo(self):
        print(self.Dryskin, self.backbone, self.softshelled)


class crocodile(Reptile):
    def __init__(self, Dryskin, backbone, softshelledeggs, hardshelled):
        super().__init__(Dryskin, backbone, backbone, softshelledeggs, hardshelled)
        self.hardshell = hardshelled

    def showinfo(self):
        print(self.hardshelled)


class fish(Animals):
    def __init__(self, height, weight, animaltype, bloodtype, water, gills):
        super().__init__(height, weight, animaltype, bloodtype)
        self.liveinwater = water
        self.hasgills = gills

    def printFish(self):
        print(self.liveinwater, self.hasgills)


class Eel(fish):
    def __init__(self, liveinwater, hasgills, electric, info):
        self.electric = electric
        super().__init__(liveinwater, hasgills)
        self.info = info

    def printEel(self):
        print(self.electric)


class Brids(Animals):
    def __init__(self, height, weight, animaltype, bloodtype, feathers, fly):
        self.feathers = feathers
        self.fly = fly
        super().__init__(height, weight, animaltype, bloodtype)

    def printBirds(self):
        print(self.feathers, self.fly)


class Eagle(Brids):
    def __init__(self, height, weight, animaltype, bloodtype, feathers, fly):
        super().__init__(height, weight, animaltype, bloodtype, feathers, fly)

    def printeagel(self):
        print(self.info)


e=crocodile("no","no","no","yes")
