class Animals:
    def __init__(self, height, weight, animaltype, bloodtype,info):
        self.height = height
        self.weight = weight
        self.animaltype = animaltype
        self.bloodtype = bloodtype
        self.info = info

    def printanimal(self):
        print(self.height, self.weight, self.animaltype, self.bloodtype)


class Reptile(Animals):
    def __init__(self, Dryskin, backbone, softshelledeggs,info):
        self.Dryskin = Dryskin
        self.backbone = backbone
        self.softshelled = softshelledeggs
        super().__init__(self.height, self.weight, self.animaltype, self.bloodtype)
        self.info = info
    def printRepltile(self):
        print(self.Dryskin, self.backbone, self.softshelled)


class crocodile(Reptile):
    def __init__(self, hardshelled,info):
        self.hardshelled = hardshelled
        super().__init__(self.Dryskin, self.backbone, self.softshelled)
        self.info = info
    def printcrocodile(self):
        print(self.hardshelled)


class fish(Animals):
    def __init__(self, water, gills,info):
        self.liveinwater = water
        self.hasgills = gills
        self.info = info
        super().__init__(self.height, self.weight, self.animaltype, self.bloodtype)

    def printFish(self):
        print(self.liveinwater, self.hasgills)


class Eel(fish):
    def __init__(self, electric,info):
        self.electric = electric
        super().__init__(self.liveinwater, self.hasgills)
        self.info = info
    def printEel(self):
        print(self.electric)



class Brids(Animals):
    def __init__(self, feathers, fly,info):
        self.feathers = feathers
        self.fly = fly
        super().__init__(self.height, self.weight, self.animaltype, self.bloodtype)
        self.info = info
    def printBirds(self):
        print(self.feathers, self.fly)


class Eagle(Brids):
    def __init__(self, feathers, fly,info):
        super().__init__(self.feathers, self.fly)
        self.info = info

    def printeagel(self):
        print(self.feathers, self.fly)


Animals(2, 100, "reptile", "o+")
crocodile('hardshelled')
Eagle()