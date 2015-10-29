class Mom:
    name = 1.0

class Dad:
    name_ = 2.0 #note that those variable cannot have the same name 

class Child(Mom,Dad):
    name_ = 3.0

suri = Child()
print suri.name
print suri.name_
