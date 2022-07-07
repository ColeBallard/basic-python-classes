import random
import time

class Animal:
    def __init__(self, species, hungry, mammal):
        self._species = species
        self._mammal = mammal
        self.__hungry = hungry

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, new_species):
        self._species = new_species

    @species.deleter
    def species(self):
        del self._species
    
    @property
    def hungry(self):
        return self.__hungry

    @hungry.setter
    def hungry(self, new_hungry):
        self.__hungry = new_hungry

    @hungry.deleter
    def hungry(self):
        del self.__hungry

    @property
    def mammal(self):
        return self._mammal

    @mammal.setter
    def mammal(self, new_mammal):
        self._mammal = new_mammal

    @mammal.deleter
    def mammal(self):
        del self._mammal

    def __lookForFood(self):
        chance = random.randint(0, 1)
        if chance == 0:
            return True
        else:
            return False

    def eat(self):
        success = self.__lookForFood()
        if success:
            self.__hungry = False
        else:
            self.__hungry = True

class Fish(Animal):
    def __init__(self, species, hungry, mammal = False):
        super().__init__(self, species, hungry, mammal)

    def swim(self):
        if self.__hungry:
            print("You didn't get very far...")
        else:
            print("You found your son!")

class Snake(Animal):
    def __init__(self, species, hungry, mammal = False):
        super().__init__(self, species, hungry, mammal)

    def slither(self):
        if self.__hungry:
            print("You didn't get very far...")
        else:
            print("You found Harry Potter!")

class Person(Animal):
    def __init__(self, species, hungry, name, mammal = True):
        super().__init__(self, species, hungry, mammal)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

    def exercise(self):
        if self.__hungry:
            print("You should eat something first...")
        else:
            print("Strength +1")

class Book:
    def __init__(self, pages):
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        self._pages = new_pages

    @pages.deleter
    def pages(self):
        del self._pages

    def readTime(self):
        return str(self._pages * 3) + " minutes"

class Textbook(Book):
    def __init__(self, pages, year, subject):
        super().__init__(self, pages)
        self._year = year
        self._subject = subject

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @year.deleter
    def year(self):
        del self._year

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        self._subject = new_subject

    @subject.deleter
    def subject(self):
        del self._subject

    def slam(self):
        if self._subject.upper() == "MATH":
            print("Numbers and equations come flying out of the top of the textbook.")
        else:
            print("Learning is hard!")

class AddressBook(Book):
    def __init__(self, pages, year, location):
        super().__init__(self, pages)
        self._year = year
        self._location = location

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @year.deleter
    def year(self):
        del self._year

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location = new_location

    @location.deleter
    def location(self):
        del self._location

    def throwAway():
        print("Who uses these things anyways?")

class Vehicle:
    def __init__(self, wheels):
        self._wheels = wheels

    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, new_wheels):
        self._wheels = new_wheels

    @wheels.deleter
    def wheels(self):
        del self._wheels

    def honk():
        print("Honk.")

class Car(Vehicle):
    def __init__(self, make, model, wheels = 4):
        super().__init__(self, wheels)
        self._make = make
        self._model = model

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @make.deleter
    def make(self):
        del self._make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @model.deleter
    def model(self):
        del self._model

    def __turnLeft(self):
        print("Turning left.")

    def __turnRight(self):
        print("Turning left.")

    def __accelerate(self):
        print("Accelerating.")

    def __brake(self):
        print("Braking.")

    def drive(self):
        for i in range(10):
            choice = random.randint(0,3)
            if choice == 0:
                self.__turnLeft()
            elif choice == 1:
                self.__turnRight()
            elif choice == 2:
                self.__accelerate()
            elif choice == 3:
                self.__brake()
            time.sleep(1)

class Bicycle(Vehicle):
    def __init__(self, mountainBike, wheels = 2):
        super().__init__(self, wheels)
        self._mountainBike = mountainBike

    @property
    def mountainBike(self):
        return self._mountainBike

    @mountainBike.setter
    def mountainBike(self, new_mountainBike):
        self._mountainBike = new_mountainBike

    @mountainBike.deleter
    def mountainBike(self):
        del self._mountainBike

    def __turnLeft(self):
        print("Turning left.")

    def __turnRight(self):
        print("Turning left.")

    def __accelerate(self):
        print("Pedaling faster.")

    def __brake(self):
        print("Braking.")

    def ride(self):
        for i in range(10):
            choice = random.randint(0,3)
            if choice == 0:
                self.__turnLeft()
            elif choice == 1:
                self.__turnRight()
            elif choice == 2:
                self.__accelerate()
            elif choice == 3:
                self.__brake()
            time.sleep(1)

class Boat(Vehicle):
    def __init__(self, weight, length, wheels = 0):
        super().__init__(self, wheels)
        self._weight = weight
        self._length = length

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @weight.deleter
    def weight(self):
        del self._weight

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        self._length = new_length

    @length.deleter
    def length(self):
        del self._length

    def goTopSpeed(self):
        print("You're going " + str((self._length * 1000)/self._weight) + " knots")

class HotAirBalloon(Vehicle):
    def __init__(self, color, wheels = 0):
        super().__init__(self, wheels)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @color.deleter
    def color(self):
        del self._color

    def pop(self):
        print("A huge, sad " + self._color + " plastic bag floats to the ground...")