#P1
class BasicClass:
    theVariable = 1

#P2
class ExampleClass:
    age = 24
    name = 'John Doe'
    location = 'Toronto, Ontario'

example_instance = ExampleClass()
print(example_instance.age)
print(example_instance.name)
print(example_instance.location)

#P3
class BirthdayBoy:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

me = BirthdayBoy('Nick',24)

print(me.age)

me.birthday()

print(me.age)

#P4
class Salesperson:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    sales = 0

    def makeSale(self,saleValue):
        self.sales += saleValue

    def salesReport(self):
        print(f'My total sales are {self.sales}!')

Delivery_boy = Salesperson('Nick','McCullum')
Delivery_boy.makeSale(600)

Delivery_boy.salesReport()
        
        
