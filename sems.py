"""""
def marks(name, sanskrit, english, telugu, maths):
    total=sanskrit+english+telugu+maths
    print(name,"total",total)

for i in range(1,11):
    name=input("enter the name")
    sanskrit= int(input("enter the marks"))
    english= int(input("enter the marks"))
    telugu = int(input("enter the marks"))
    maths = int(input("enter the marks"))
    marks(name,sanskrit,english,telugu,maths)
"""""


class Marks:
    def __init__(self, name, sanskrit, english, telugu, maths):
        self.name = name
        self.english = english
        self.hindi = hindi
        self.telugu = telugu
        self.maths = maths
        self.total = int(input("enter the total marks"))

    def scored(self):
        scored = self.hindi + self.english + self.telugu + self.maths
        print(self.name, "scored", scored)

    def average(self):
        average = (self.hindi + self.english + self.telugu + self.maths) / 4
        print(self.name, "average", average)

    def percentage(self):
        percent = ((self.hindi + self.english + self.telugu + self.maths) / self.total)*100
        print(self.name, "percentage", percent)


s1 = Marks("dan", 90, 92, 89, 84)
s1.scored()
s1.average()
s1.percentage()
# s2 = Marks("ary", 90, 80, 70, 75)
# s2.total()
# s2.average()
