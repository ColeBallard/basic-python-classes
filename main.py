import random
import time

class Animal:
    def __init__(self, name, species, mammal):
        self._name = name
        self._species = species
        self._mammal = mammal

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

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
    def mammal(self):
        return self._mammal

    @mammal.setter
    def mammal(self, new_mammal):
        self._mammal = new_mammal

    @mammal.deleter
    def mammal(self):
        del self._mammal

    def __lookForFood(self):
        if self._mammal:
            return True
        else:
            return False

    def eat(self):
        success = self.__lookForFood()
        if success:
            print("I'm full!")
        else:
            print("I'm still hungry.")

class Book:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre
        self.__pages = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_genre):
        self._genre = new_genre

    @genre.deleter
    def genre(self):
        del self._genre

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, new_pages):
        self.__pages = new_pages

    @pages.deleter
    def pages(self):
        del self.__pages

    def readTime(self):
        return str(self.__pages * 3) + " minutes"

class Vehicle:
    def __init__(self, name, make, model):
        self._name = name
        self._make = make
        self._model = model

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

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
        for i in range(100):
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