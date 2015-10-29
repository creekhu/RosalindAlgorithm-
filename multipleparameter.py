#treat *var as a tuple 

def count(*var):
    print var

count('hey','man','I\'hungry','as','deerbra')

def ver2(name, *ver2):
    print name
    print ver2
    
#print out a tuple
ver2('creek',2,3,4,5)

#convert parameter into a dictionary
#use double asterid
def convert(**var):
    print var

#format: key = value
convert(apples = 2, baanana = 3, hog = 5)

def more(firstname, lastname, *height, **preference):
    print firstname
    print lastname
    print height
    print preference

more('tianqi','hu', 180,190,200,210, kevin = 'hello',hart = 'hey',tianqi = 2)


#tuple as parameter
def test(a,b,c):
    print a+b+c

list = (2,3,4)
test(*list)

#pass in dictionary
def know(**a):
    print a
    
test = {'hello' : 2, 'hey' : 3}
know(**test)






