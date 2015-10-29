string = raw_input("")
list_1 = list(string)
list_2 = []
list_3 = []

i = 0

while i < len(list_1):
    temp = list_1[i] + list_1[i+1] + list_1[i+2]
    list_2.append(temp)
    i = i + 3

print list_2

i = 0
while i < len(list_2):
    
    if list_2[i] == 'UUU' or list_2[i] == 'UUC':
        list_3.append('F')
        i = i+1
        
    elif list_2[i] == 'UUA' or list_2[i] == 'UUG':
        list_3.append('L')
        i = i+1
        
    elif list_2[i] == 'UCU' or list_2[i] == 'UCC' or list_2[i] == 'UCA' or list_2[i] == 'UCG':
        list_3.append('S')
        i = i+1

    elif list_2[i] == 'UAU' or list_2[i] == 'UAC':
        list_3.append('Y')
        i = i+1

    elif list_2[i] == 'UAA' or list_2[i] == 'UAG' or list_2[i] == 'UGA':
        #list_3.append('Stop')
        i = i+1
        
    elif list_2[i] == 'UGU' or list_2[i] == 'UGC':
        list_3.append('C')
        i = i+1

    elif list_2[i] == 'UGG':
        list_3.append('W')
        i = i+1

    elif list_2[i] == 'CUU' or list_2[i] == 'CUC' or list_2[i] == 'CUA' or list_2[i] == 'CUG':
        list_3.append('L')
        i = i+1

    elif list_2[i] == 'CCU' or list_2[i] == 'CCC' or list_2[i] == 'CCA' or list_2[i] == 'CCG':
        list_3.append('P')
        i = i+1

    elif list_2[i] == 'CAU' or list_2[i] == 'CAC':
        list_3.append('H')
        i = i+1

    elif list_2[i] == 'CAA' or list_2[i] == 'CAG':
        list_3.append('Q')
        i = i+1

    elif list_2[i] == 'CGU' or list_2[i] == 'CGC' or list_2[i] == 'CGA' or list_2[i] == 'CGG' or list_2[i] == 'AGA' or list_2[i] == 'AGG':
        list_3.append('R')
        i = i+1

    elif list_2[i] == 'AUU' or list_2[i] == 'AUC' or list_2[i] == 'AUA':
        list_3.append('I')
        i = i+1
        
    elif list_2[i] == 'AUG':
        list_3.append('M')
        i = i+1

    elif list_2[i] == 'ACU' or list_2[i] == 'ACC' or list_2[i] == 'ACA' or list_2[i] == 'ACG':
        list_3.append('T')
        i = i+1

    elif list_2[i] == 'AAU' or list_2[i] == 'AAC':
        list_3.append('N')
        i = i+1

    elif list_2[i] == 'AAA' or list_2[i] == 'AAG':
        list_3.append('K')
        i = i+1

    elif list_2[i] == 'AGU' or list_2[i] == 'AGC':
        list_3.append('S')
        i = i+1

    elif list_2[i] == 'GUU' or list_2[i] == 'GUC' or list_2[i] == 'GUA' or list_2[i] == 'GUG':
        list_3.append('V')
        i = i+1

    elif list_2[i] == 'GCU' or list_2[i] == 'GCC' or list_2[i] == 'GCA' or list_2[i] == 'GCG':
        list_3.append('A')
        i = i+1

    elif list_2[i] == 'GAU' or list_2[i] == 'GAC':
        list_3.append('D')
        i = i+1

    elif list_2[i] == 'GAA' or list_2[i] == 'GAG':
        list_3.append('E')
        i = i+1
    else:
        list_3.append('G')
        i = i+1

print list_3
string = ''.join(list_3)
print string

    
    

    
    

    
    
    
