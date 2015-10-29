class momClass:
    height = 1.0
    name = 'mother'

class dadClass:
    height = 2.0
    name = 'father'
    
class childClass(momClass):
    pass #if you have nothing to do 

class childClass(dadClass):
    name = 'suri'

                 
suri = childClass()
print suri.name
print suri.height

