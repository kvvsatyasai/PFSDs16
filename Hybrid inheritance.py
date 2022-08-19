class Veera:
    def veera(self):
        print("this is veera class")
class Venkata(Veera):
    def venkata(self):
        print("this is venkata class")
class Satya(Veera):
    def satya(self):
        print("this is satya class")
class Final(Venkata,Satya):
    def final(self):
        print("this is final class")
obj=Final()
obj.final()
obj.veera()
obj.venkata()
obj.satya()



