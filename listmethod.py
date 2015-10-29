numbers = [1,2,3,4,5,6,7]
print len (numbers)
print max(numbers)
print min(numbers)

#change one value in the list
numbers[5] = 0
print numbers

#del an element in the list
del numbers[0]
print numbers

#conver a string to a list of letters

a = list('creek')
print a 

#append method
numbers.append(4)
print numbers

#count method count the occurence of certain paramenter
print numbers.count(1)


one = [1,2,3]
two = [4,5,6]
#it is not a good idea to do something like that 
one.append(two)
print one
print one[3]

one = [1,2,3]
one.extend(two)
print one 
