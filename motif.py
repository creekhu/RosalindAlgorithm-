string_1 = raw_input("Enter the first string: ")
string_2 = raw_input("Enter the second string: ")

list_1 = list(string_1)
list_2 = list(string_2)
list_3 = []

i = 0
k = 0
stringblank = ''

while k <= len(list_1) - len(list_2):
    
    temp1 = list_2[:len(list_2)]
    temp2 = list_1[k:len(list_2)+k]
    string1 = ''.join(temp1)
    string2 = ''.join(temp2)
    
    if string1 == string2:
        
        list_3.append(str(k+1))
        
        k = k + 1
        
    else:
        k = k + 1

print list_3
string = ' '.join(list_3)
print string
            
