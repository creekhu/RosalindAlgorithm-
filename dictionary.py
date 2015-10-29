#dic = {'key' : 'value'}
#use curly brace to declare the dictionary 
book = {'dad':'bob','mom':'lisa','bro':'joe'}

temp = book['dad']
print temp 
temp = book['bro']
print temp

#copy the entire list to a new list 
newDic = book.copy()
print newDic

#clear the entire list 
book.clear()
print book

a = newDic.has_key('dad')
b = newDic.has_key('mom')
print a
print b

