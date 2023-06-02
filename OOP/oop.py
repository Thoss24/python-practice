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

