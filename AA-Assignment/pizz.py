class Pizza:

    def __init__(self, itemid, category, type, size):
        self.type = str(type)
        self.itemid = int(itemid)
        self.category = str(category)
        self.size = str(size)

    class Size:
        def __init__(self, small, medium, large):
            self.small = small
            self.medium = medium
            self.large = large

    class Category:
        def category(self, veg, nonveg):
            self.veg = veg
            self.nonveg = nonveg


class Veg(Pizza):
    class ValidateSize(Pizza.Size):
        def ValidateSize(self):
            return Pizza.Size

    class ValidateType(Pizza):

        def __init__(self, VegStuffed, VegNotStuffed, itemid, category, type, size):
            super().__init__(itemid, category, type, size)
            self.VegStuffed = VegStuffed
            self.VegNotStuffed = VegNotStuffed

        def ValidateType(self, VegStuffed, VegNotStuffed):
            return Pizza

    class ValidateCategory(Pizza.Category):
        def __init__(self, veg):
            super(Pizza.Category)


class IdentifyCost(Veg):
    Veg.ValidateSize()
    Veg.ValidateType()



class NonVeg(Pizza):
    class ValidateSize(Pizza.Size):
        def ValidateSize(self):
            return Pizza.Size

    class ValidateType(Pizza):

        def __init__(self, NonVegStuffed, NonVegNotStuffed, itemid, category, type, size):
            super().__init__(itemid, category, type, size)
            self.NonVegStuffed = NonVegStuffed
            self.NonVegNotStuffed = NonVegNotStuffed

        def ValidateType(self, NonVegStuffed, NonVegNotStuffed):
            return Pizza

    class ValidateCategory(Pizza.Category):
        def __init__(self, veg):
            super(Pizza.Category)


p1 = Pizza()
