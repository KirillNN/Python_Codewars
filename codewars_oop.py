# https://proglib.io/p/python-oop/
# class Human:
#     pass
#
#
# class Man(Human):
#     pass
#
#
# class Woman(Human):
#     pass
#
#
# def God():
#     return [Man(), Woman()]
#
#
# class Hero(object):
#     def __init__(self, name='Hero'):
#         self.name = name
#         self.position = '00'
#         self.health = 100
#         self.damage = 5
#         self.experience = 0
#
#
# myHero = Hero('dsc',234,234,234,234)
# myHero = Hero()
#
#
# class Person(object):
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"
#
#     def getInfo(self):
#         return 'johns age is 34'
#
#
# person = Person('john', 16)
#
# print(person.info)
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + ' meows.'


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives == 0:
            raise Exception('Omae wa mo shindeiru')
        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False


# guesser = Guesser(10, 2)
# guesser.guess(1)
# guesser.guess(2)
# guesser.guess(10)


class Dog():
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return "Woof"


snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")

# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python
import random


class Ghost(object):
    def __init__(self, color=''):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghosts = [Ghost().color for _ in range(100)]
print(ghosts)
