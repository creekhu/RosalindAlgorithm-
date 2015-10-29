b = 1

while b <= 10:
    print b
    b = b+1
    

show = ['nigga','rider','deerbra','subway']
for var in show:
    print "sup " + var

dic = {'kevin':'nigga','hrat':'show','creek':'sup'}

for key in dic:
    print key, dic[key]


#test infinite loop

while 1:
    name = raw_input('Enter name: ')
    if name == 'quit':
        break
    else:
        print 'sup nigga'
        
