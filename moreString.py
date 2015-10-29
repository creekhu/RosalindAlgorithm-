#customize the string

kevin = "help %s, help %s, %s"
hart = ('deer','zebra','nigga')
# print string missing variable % supplement 
print kevin % hart

#find method: find stuff in string

string = 'hey sup man'
#a is the first occurence of the searching word 
a = string.find('hey')
print a

#join method
seq = ['hey','sup','man','nigga']
glue = 'kevin' #join kevin after every single word in seq
print glue.join(seq)

s = 'sup NIGGA HOW\'s your dat going'
temp = s.lower()
print temp

code = 'the code is man, I\'m hungry as shit. man, I\'m hungry as shit'
temp = code.replace('man','nigga')
print temp
