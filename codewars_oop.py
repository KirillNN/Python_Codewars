# # https://proglib.io/p/python-oop/
# # class Human:
# #     pass
# #
# #
# # class Man(Human):
# #     pass
# #
# #
# # class Woman(Human):
# #     pass
# #
# #
# # def God():
# #     return [Man(), Woman()]
# #
# #
# # class Hero(object):
# #     def __init__(self, name='Hero'):
# #         self.name = name
# #         self.position = '00'
# #         self.health = 100
# #         self.damage = 5
# #         self.experience = 0
# #
# #
# # myHero = Hero('dsc',234,234,234,234)
# # myHero = Hero()
# #
# #
# # class Person(object):
# #     def __init__(self, name, age):
# #         self.info = f"{name}s age is {age}"
# #
# #     def getInfo(self):
# #         return 'johns age is 34'
# #
# #
# # person = Person('john', 16)
# #
# # print(person.info)
# #
# #
# # class Cat(Animal):
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def speak(self):
# #         return self.name + ' meows.'
#
#
# class Guesser:
#     def __init__(self, number, lives):
#         self.number = number
#         self.lives = lives
#
#     def guess(self, n):
#         if self.lives == 0:
#             raise Exception('Omae wa mo shindeiru')
#         if n == self.number:
#             return True
#         else:
#             self.lives -= 1
#             return False
#
#
# # guesser = Guesser(10, 2)
# # guesser.guess(1)
# # guesser.guess(2)
# # guesser.guess(10)
#
#
# class Dog():
#     def __init__(self, breed):
#         self.breed = breed
#
#     def bark(self):
#         return "Woof"
#
#
# snoopy = Dog("Beagle")
#
# scoobydoo = Dog("Great Dane")
#
# # https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python
# import random
#
#
# class Ghost(object):
#     def __init__(self, color=''):
#         self.color = random.choice(["white", "yellow", "purple", "red"])
#
#
# ghosts = [Ghost().color for _ in range(100)]
# print(ghosts)
#
#


class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))

volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.name)
# Output:
# Volga
# Seine
# Nile


volga.get_info()
# The length of the Volga is 3530 km
seine.get_info()
# The length of the Seine is 776 km
nile.get_info()
# The length of the Nile is 6852 km

# self.method()
volga.get_info()
# The length of the Volga is 3530 km

# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km

print(River.name)  # AttributeError

volga.name  # "Volga"
seine.name  # "Seine"
nile.name   # "Nile"


# basic method syntax
class MyClass:
    # the constructor
    def __init__(self, arg1):
        self.att = arg1

    # custom method
    def do_smt(self):
        # does something

my_object = MyClass(some_value)
# calling the instance method

# В этом примере экземпляр my_object передается неявно, поэтому мы не пишем параметр в коде.
my_object.do_smt()
# my_object does something

# Однако мы можем передать экземпляр явно:
MyClass.do_smt(my_object)
# my_object does the same thing

# Эти примеры ясно показывают, почему self должен быть первым аргументом методов экземпляра.
# Если вы хотите, чтобы у вашего метода были другие параметры, просто напишите их после ключевого слова self!


# class and its methods
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))


# function
def sail_function(name):
    print("{} has sailed!".format(name))

# creating an instance of the class Ship
# and calling the method sail
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail()
# prints "Black Pearl has sailed!"


# calling the function sail_function
sail_function(black_pearl.name)
# also prints "Black Pearl has sailed!"

# Пока что метод не вернул никаких значений, так как мы использовали только функцию print ().
# Очевидно, что, как и в случае с функциями, мы можем определить, какой тип данных может возвращать метод, 
# с помощью оператора return. Например, создадим метод, который вычисляет, сколько килограммов груза находится на корабле 
# (изначально вес груза указывается в тоннах):
class Ship:
    # other methods
    
    def convert_cargo(self):
        return self.cargo * 1000

# Метод прост: он переводит тонны в килограммы (умножая на 1000), а затем возвращает рассчитанное значение. 
# Если бы мы ее вызывали, мы не получали бы никаких сообщений, если бы явно не напечатали результат функции:
print(black_pearl.convert_cargo())  # 0
# Поскольку мы не изменили значение по умолчанию для атрибута cargo, метод вернет 0, умноженный на 1000, что также равно 0.

# Методы внутри классов определяют поведение класса или его объектов. Они похожи на функции, за исключением того, 
# что они сильно связаны с классом и не могут быть вызваны независимо от него или его экземпляров.
# Первым параметром методов экземпляра является ключевое слово self, которое представляет конкретный экземпляр класса. 
# Этот конкретный экземпляр класса является первым аргументом, передаваемым методу. Методы могут возвращать значения или 
# просто печатать сообщения (т.е. ничего не возвращать).
# Методы позволяют добавлять в классы любую функциональность. Вот как вы можете манипулировать своими объектами и создавать 
# сложные программы, поэтому мы рекомендуем вам изучить методы в своих проектах!
