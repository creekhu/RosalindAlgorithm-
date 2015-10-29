#slice[x,y] x inclusive y exclusive 

example = [0,1,2,3,100,5,6,7,8,9]
print example[4:8]

# to slice the last element in the list
# allowing  n+1 index

print example[4:10]

#if you want to slice bakcward and include the last element in the list
#leave the number blank

print example[-5:]

#slice without knowing the first element of the list till the destination

print example[:4]

#shortcut to get entire list

print example[:]

#using three parameters; the third one stands for the incrementation
#index+2 for each time

print example[1:10:2]

# reverse
print example[10:0:-2]

# shortcut for going backward

print example[::-2]

print example[::-3]
