'''class smartdevice:
    def __init__(self, brand, price):
        self.brand=brand
        self.price = price
    def recharge(self):
        print("Elctron are Yummy!")

class watch(smartdevice):
    def __init__(self, brand, price,has_gps):
        smartdevice.__init__(self, brand,price)
        self.step_count=0
        self.has_gps = has_gps

my_watch = watch("Fitband",200, False)
print(my_watch.brand)
my_watch.recharge()'''

'''class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        print(f'{self.name} is eating')

class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color=color 
    def meow(self):
        print("meow")

dog = Animal("Doggy", "Lepard")
cat1 = Cat("Kitty","Deshi", "White")
print(cat1.color)
cat1.eat()
cat1.meow()
dog.eat() '''

class A:
    def method_a(self):
        print("this is method a")

class B:
    def method_b(self):
        print("this is method b")
class C(A,B):
    def method_c(self):
        print("this is method c")

obj = C()
obj.method_a()
obj.method_b()
obj.method_c()