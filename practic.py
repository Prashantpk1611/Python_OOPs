class India:
    def currency(self):
        print("Currency is Ruppee")
    def language(self):
        print("Language is Hindi")
    def capital(self):
        print("Capital is New Delhi")

class Russia:
    def currency(self):
        print("Curreny is Ruble")
    def language(self):
        print("Language is Russian")
    def capital(Self):
        print("Capital is Mascow")

def f_call(obj):
    obj.currency()
    obj.language()
    obj.capital()

obj1 = India()
f_call(obj1)
obj2 = Russia()
f_call(obj2)