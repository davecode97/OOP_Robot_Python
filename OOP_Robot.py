# David
# Guadalajara, Mex 2020

class Robot:
    # -----Constructor
    def __init__(self, Name, Color, Weight):
        self.name = Name
        self.color = Color
        self.weight = Weight

    def introduce_Self(self):
        print("My name is "+self.name)

#----- Instances
r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)


class Person:
    # ------Contructor
    def __init__(self, Name, Personality, IsSitting):
        self.name = Name
        self.personality = Personality
        self.isSitting = IsSitting

    def sitDown(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False

#---- Instances
p1 = Person("Alice", "Agressive", False)
p2 = Person("Becky", "Talkactive", True)

#---- Owners
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_Self()
p2.robot_owned.introduce_Self()

#----- Follow
r1.LokingAt = r1
r2.LokingAt = r2

