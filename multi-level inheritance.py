class ClassA:
    def satya(self):
        print("this is classA")
class ClassB(ClassA):
    def sai(self):
        print("this is classB")
class ClassC(ClassB):
    def kvv(self):
        print("this is classC")
class ClassD(ClassC):
    def satyasai(self):
        print("this is classD")
obj=ClassD()
obj.satya()
obj.sai()
obj.kvv()
obj.satyasai()