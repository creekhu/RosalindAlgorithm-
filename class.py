class real:
    height = 109
    weight = 115

    def method(self):
        return 'sup man'

classobject = real()

print classobject.height
print classobject.weight

a = classobject.method()
print a 


#注意self.name的用法

class name:
    name = None
    def __init__
    def createName(self,name):
        self.name = name
    def displayName(self):
        return self.name
    def printName(self):
        print 'hello %s' % self.name

hello = name()
#print hello.displayName()
hello.createName('creek')
print hello.displayName()
hello.printName()
