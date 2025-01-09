class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cord = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cord = [self.speed * dx, self.speed * dy, self.speed * dz]
        if self._cord[2] < 0:
            print(f"It's too deep, i can't dive :(")
            self._cord[2] = 0

    def get_cord(self):
        print(f'X: {self._cord[0]}, Y: {self._cord[1]}, Z: {self._cord[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, i am peacefil')
        else:
            print('Be careful, i am attacking you 0_0')

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        import random
        eggs = random.randint(1, 4)
        if eggs >= 2:
            print(f'Here are {eggs} eggs for you')
        else:
            print(f'Here is {eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        import math
        self._cord[2] = abs(self._cord[2] // self.speed) - dz // 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cord()
db.dive_in(6)
db.get_cord()
db.lay_eggs()
