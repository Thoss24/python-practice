# encapsulation of methods and restricted variables
class Test:
    var1 = None
    _var2 = None
    __var3 = None

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    def public(self):
        print("Public: ", self.var1)
    
    def _protected(self):
        print("Protected: ", self._var2)

    def __private(self):
        print("Private: ", self.__var3)

    def accessPrivate(self):
        self.__private()

class Sub(Test):

    def __init__(self, var1, var2, var3):
        Test.__init__(self, var1, var2, var3)
    
    def accessProtected(self):
        self._protected()


obj = Sub("ABC", 4, "EFG!")

obj.public()
obj.accessProtected()
obj.accessPrivate()

# basic class with instances
class Country:
    country_name = ""
    country_capital = ""
    country_currency = ""

    def __init__(self, name):
        self.country_name = name

    def currency_capital(self, currency, capital):
        self.country_currency = currency
        self.country_capital = capital
    
    def print_data(self):
        print("Country Name: ", self.country_name)
        print("Country Currency: ", self.country_currency)
        print("Country Capital: ", self.country_capital)

UK = Country('UK')
USA = Country("America")

UK.currency_capital("British Pound", "London")
USA.currency_capital("US Dollar", "Washington DC")
UK.print_data()
USA.print_data()


#inheritance allows us to define a class that inherits all the methods and properties from another class
class Parent:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    def print_name(self):
        print(self.firstName, self.lastName)

parent = Parent("Thomas", "Fogarty")
parent.print_name()

class Child(Parent):
    pass

child = Child("Boy", "Bear")
child.print_name()

# multilevel inheritance
class Grandfather:
    def __init__(self, gname):
        self.gname = gname

class Father(Grandfather):
    def __init__(self, fname, gname):
        self.fname = fname
    
        Grandfather.__init__(self, gname)

class Son(Father):
    def __init__(self, sonname, fname, gname):
        self.sonname = sonname

        Father.__init__(self, fname, gname)

    def print_name(self):
        print("Grandfather name: ", self.gname)
        print("Father name: ", self.fname)
        print("Son name: ", self.sonname)


derived = Son("Thomas", "Stephen", "Paul")
derived.print_name()


class Provider:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
    
    def print_capital_country(self):
        print(self.capital + " is the capital of", self.country)

class Receiver(Provider):
     pass

receive = Receiver("England", "London")   
receive.print_capital_country()

#polymorphism allows for multiple classes with the same method name
class Car:
    def __init__(self, car):
        self.car = car
    
    def print_item(self):
        print(self.car)

class Boat:
    def __init__(self, boat):
        self.boat = boat
    
    def print_item(self):
        print(self.boat)

class Plane:
    def __init__(self, plane):
        self.plane = plane
    
    def print_item(self):
        print(self.plane)

car = Car("Mustang")
boat = Boat("Sunseeker")
plane = Plane("Boeing 747")

for x in (car, boat, plane):
    x.print_item()