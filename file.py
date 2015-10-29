# open('path', 'read' or 'write')

#fileobject = open('c:/Python27/Python Learning/test.txt','w')
#fileobject.write('hello world')
#fileobject.close()

f = open('c:/Python27/Python Learning/test.txt','r')
string = f.read().split('>Rosalind_')[1:]
print string[0][4:]
f.close()
