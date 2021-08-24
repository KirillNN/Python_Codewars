#########################Creating attributes with methods###################################

# Атрибуты экземпляра - это те, которые определены в методах, поэтому по определению 
# мы можем создавать новые атрибуты внутри наших пользовательских методов. В качестве примера возьмем класс Ship.
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # Каждому кораблю нужен капитан, поэтому давайте определим для этих целей метод name_captain:
    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))

# При первом вызове метод name_captain создает новый атрибут с именем captain и печатает соответствующее сообщение.
# При следующем использовании он просто изменяет значение атрибута self.captain (а ​​также печатает сообщение).
# Чтобы увидеть, как это будет работать, давайте создадим корабль «Black Pearl»:
black_pearl = Ship("Black Pearl", 800)

# Если бы мы сейчас попытались распечатать значение атрибута captain, то получили бы ошибку:
print(black_pearl.captain)  # AttributeError

# Это потому, что этот атрибут создается только в методе name_captain. Если мы его вызовем, мы сможем получить 
# доступ к атрибуту captain:
black_pearl.name_captain("Jack Sparrow")
# prints "Jack Sparrow is the captain of the Black Pearl"
print(black_pearl.captain)  # "Jack Sparrow"
# Обратите внимание, что только те экземпляры, которые вызвали этот метод, будут иметь атрибут captain. 
# Об этом важно помнить! Вы можете получить сообщение об ошибке, если попытаетесь использовать атрибут, 
# а метод еще не был вызван.

# Чтобы избежать этих проблем, рекомендуется определить все возможные атрибуты в файле __init__.
# Это может не только помочь вам избежать AttributeError, но также дает хорошее понимание класса и его объектов
# с самого начала. Если вы действительно хотите создать значение атрибута в специальном методе экземпляра,
# укажите его в __init__ как None:
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

#####################################################Modifying attributes with methods############################
# Методы также можно использовать для изменения атрибутов экземпляра. Возьмем, к примеру, методы load_cargo и unload_cargo:
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")

# Оба этих метода должны изменять значение атрибута cargo, если эти изменения возможны.
# Метод load_cargo сначала проверяет, что загрузка определенного веса не превышает вместимость корабля,
# а unload_cargo проверяет, что разгрузка не сделает вес груза отрицательным. Затем они оба вносят изменения
# или выводят сообщение о том, что эти изменения невозможны.
# example
black_pearl.load_cargo(600)
# "Loaded 600 tons"

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"

black_pearl.load_cargo(700)
# "Cannot load that much"

black_pearl.unload_cargo(300)
# "Cannot unload that much"

# Пока наши методы не возвращали никаких значений, поскольку мы использовали только функцию print (),
# но мы можем заставить наши методы возвращать любой тип значения, который мы хотим. Например, давайте создадим метод,
# который вычисляет, сколько еще груза может загрузить наш корабль.
class Ship:
    # all other methods
    
    def free_space(self):
        return self.capacity - self.cargo

# Если бы мы вызывали этот метод в нашем Black Pearl, мы бы не получили никаких сообщений, потому что метод ничего
# не печатает. Но вместо этого мы могли бы использовать возвращаемое значение в наших дальнейших вычислениях. 
# Мы могли бы, например, переписать метод load_cargo, используя метод free_space:
class Ship:
    # updated load_cargo method
    def load_cargo(self, weight):
        if weight <= self.free_space():
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")
# В этом примере мы вызвали метод внутри другого метода и использовали значения в наших вычислениях.
# Опять же, мы использовали self, чтобы убедиться, что мы имеем дело только с конкретным экземпляром класса Ship
# и что все вычисления относятся к этому экземпляру.









































