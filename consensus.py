f = open('c:/Python27/Python Learning/test.txt','r')
string = f.read().split('>Rosalind_')[1:]
f.close()

string1 = string[0][2:-2]
string2 = string[1][1:-2]
string3 = string[2][1:-2]
string4 = string[3][1:-2]
string5 = string[4][1:-2]
string6 = string[5][1:-2]
string7 = string[6][1:-2]
#string8 = string[7]
#string9 = string[8]
#string10 = string[9]

list1 = list(string1)
list2 = list(string2)
list3 = list(string3)
list4 = list(string4)
list5 = list(string5)
list6 = list(string6)
list7 = list(string7)
#list8 = list(string8)
#list9 = list(string9)
#list10 = list(string10)

matrix = [list1] + [list2] + [list3] + [list4] + [list5] + [list6] + [list7] #+ [list8] + [list9] + [list10]
print matrix
print len(matrix)

listA = [0] * len(list1)
listC = [0] * len(list1)
listG = [0] * len(list1)
listT = [0] * len(list1)

i = 0
while i < len(matrix):
    
    k = 0
    
    while k < len(list1):
        if matrix[i][k] == 'A':
            listA[k] = listA[k] + 1
            k = k + 1
            
        elif matrix[i][k] == 'C':
            listC[k] = listC[k] + 1
            k = k + 1
            
        elif matrix[i][k] == 'G':
            listG[k] = listG[k] + 1
            k = k + 1
            
        elif matrix[i][k] == 'T':
            listT[k] = listT[k] + 1
            k = k + 1

        else:
            pass

    i = i + 1

i = 0
listtemp = []
while i < len(list1):
    if listA[i] == max(listA[i],listC[i],listG[i],listT[i]):
        listtemp.append('A')
        i = i + 1

    elif listC[i] == max(listA[i],listC[i],listG[i],listT[i]):
        listtemp.append('C')
        i = i + 1

    elif listG[i] == max(listA[i],listC[i],listG[i],listT[i]):
        listtemp.append('G')
        i = i + 1

    elif listT[i] == max(listA[i],listC[i],listG[i],listT[i]):
        listtemp.append('T')
        i = i + 1
    else:
        i = i + 1
        
output = ''.join(listtemp)
print output

stringA = ''.join(str(listA))
stringC = ''.join(str(listC))
stringG = ''.join(str(listG))
stringT = ''.join(str(listT))

print 'A: ' + stringA
print 'C: ' + stringC
print 'G: ' + stringG
print 'T: ' + stringT

        

    
    

