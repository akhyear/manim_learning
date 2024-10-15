# class phone:
#     def hard_work(self):
#         print("Myphone is Xiomi")
# my_phone=phone()
# my_phone.hard_work()

# class calculator:
#     brand = "Casio"
#     def add(self,a,b):
#         return a+b
# my_calc = calculator()
# sum = my_calc.add(1,9) 
# print(sum)

# class bank:
#     ac = 1000
#     def get_balance(self, a):
#         return self.ac + a
# my_account = bank()
# new_balance = my_account.get_balance(99)
# print(new_balance) 

# class shopping:
#     cart=[]
#     def add_cart(self,item):
#         self.cart.append(item)
#         return self.cart

# customer1 = shopping()
# customer2 = shopping()

# print(customer1.add_cart("Bag"))
# print(customer2.add_cart("Shoe"))

# class shopping:
#     def __init__(self):
#         self.cart = []
#     def add_cart(self,item):
#         self.cart.append(item)
#         return self.cart
# customer1 = shopping()
# customer2 = shopping()

# a= customer1.add_cart("Juta")
# b = customer2.add_cart("muja")
# print(a)
# print(b)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         return f"my name is {self.name} and my age {self.age}"

# persion1 = person("Rafin",25)
# a = persion1.introduce()
# print(a)

class bank:
    def __init__(self):
        self.minimum = 100
        self.balance = 1000
    def get_balance(self):
        return self.balance

    def withdrawl(self,ammount):
        if ammount<self.minimum:
            print("No money for you")
        elif ammount > self.balance:
            print("You are broke")
        else:
            self.balance = self.balance - ammount

my_bank = bank()
my_bank.withdrawl(66)
balance = my_bank.get_balance()
print(balance)