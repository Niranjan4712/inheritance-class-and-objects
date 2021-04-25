class Ravi:
    def felixMethod(self):
        print('This is from Ravi class')
class Vijay(Ravi):
    def felixItMethod(self):
        print('This is from Vijay class')
class Niranjan(Vijay):
    def felixSystemMethod(self):
        print('This is from Niranjan class')
class Rohan(Niranjan):
    def felixnewMethod(self):
        print('This is from Rohan class')

f=Rohan()
f.felixMethod()
f.felixItMethod()
f.felixSystemMethod()
f.felixnewMethod()