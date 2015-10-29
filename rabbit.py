listnum = [1,1]
i = 0
while i < 40:
    listnum.append(listnum[i]*2+listnum[i+1])
    i = i+1

print listnum
print listnum[35]


