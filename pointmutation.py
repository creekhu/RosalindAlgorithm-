a = 'TCCGTAATTCAGAGCTACGGATAGACTGTTCCAGTGGCCCAGCGTGAACAGATTCATGCTTGTCGGCAGCCCTGTGCAGAATTATATTCTCTTACCACTAAACAGTTCCCCACTCTTTACTTAAATCAACGACGACCGTACGAAGTCTCTGTGTATAGAAGAGTGGCATAGCCGAATGAATATGCCGGGTCGTGTTGAGGTACTATGATGTCCCAAGACGATTTTTCCAGCATTGTCTCATTCGTGTCGCAGAGAATGCAACGTCGCTTCGAAATTTAGCTGCGCTGCGAAGTTGTGTCGCACGTTCGTGAAGGGGATGGGCTACTACGTCGAGATGAAAGTGATGCGGGAAGTTGGACCGCTGTCGCGTGGAAGTTGGTCGGATAAAAAATATAGTCTAATACTGAACATGGTTAGGTGCTATATCGCGCTGCCTACACGTAAACGGCGCGTCTTAGATTGATGACACCAGTAAACGTATTCCCGTCAGATGTATGAAACTCTTCTAATCTCGTGCGGTACGGCATAGAGAACGTTTACCAGGAGCATTCAACCTTTGTGTGGGAAAACGCCTGCCGTAAGAAGGCCAGTACTACAACGTGAGTTTTATAGATACTTACATGTATAGCCGTGCCCGAAGAAAGTTATGATCTCCATGACCTTAATCAATTCTAAGCGGCGTCGCTCACTGTCTATTGCAAGAGGTTGGATGATATCCGCATGAATGGAGCGTTGATCGGGCTTAGCCACTGGATAAATATACGCTCTTTCCCGCTTAGGTTCCCCTGGTACGTGGTACAACTTTTAAAATAGTCAACCATTTATAACGCAACGTACTGGGAGGTTTCTTTAGTACCGTATTCCCCCAAGCTCGTTTAGACGCATTGACGATGACACCAGAAGCAAGAGGTATGTTGCAGTAGTTATTGCTAAACGCTAATAAATAGCCTAAAAGATTATTTCTGCCT'
list_1 = list(a)

b = 'TGCGGAAGACGTTGCTACTGATAGGAGTTGCGAGGATACCAGCGCAAACTTTTGCATGGACCGCTATGGCGTTGGGGGGGATGTTGTGGATCCCCCCACCAAGATTGCCCCAAGAGTTAGTAAAATAGAAGCCTTGCGGCTATAATCGCGCAGTTGAATAGCACCCCACAGTAGTATGGTAATTGGTTGTCGTCTTATGTTAAAATTTTGCCCTATTAGCCCTTGGGCCTCATGTTGGCATTACGGAGGAGATGTAGGCACCGCCGCGTCGAATTTAGGCCGGAGTGTAGGGTTGTCATGCTAGCACATGGAGTCTCCTGACACCACCAACGTGGTGGCTGTTAAACGTGGCCTTCCAAGGCGCAGTCGGCGAATTTCTAGGGTTAGTTGTGCTAGACCAAGCCTGAGCATCGACCGCTGCGCTCGCCCATGGCCTCGTTGAGAATAGCACTTCTCAGCTGTATTATACCGGCTATCGCGTATCAGTCCCATAAATAAATGTCTCCTCGACTCTGACGAGATAGGGAAGCGAGCGGTTACTCGCTTCCTCCAACCTAAGTGTGGAAAATAGGTTGCTGGACTCCCGGTAATAACTTAAGGTAATTATGATAGATACTTTGGAGGCTATACGTCAACGACGGCAGTGAAGACATACCTTACCTCTTGGCCGCCCGAGTTGGGTGGACAATTGTAGTGACGAAGAGGTTGTATGACATACGTGTGAATAATGAGGACACCATCGTTGCCGGAGGGCTTAGGAGTCGAACTCTCGAGCTTCGATAGCTGCTCTACGGAGCATAGGTAGTGACATAATCAAATATTCGCATCGCATCATAATCGAACGTTTATATCTAACATCATCTAGGTCCGACCTGTAGCAGCCTACGGGTAATCGTACAGAATCGAGCAATAAGGTGGAGGGGGTTTAGTACACCGCAAATCCCTAACCTAAGTCATGAGATCTATCG'
list_2 = list(b)

i = 0
num = 0

while i < len(list_1):
    if list_1[i] != list_2[i]:
        i = i + 1
        num = num + 1
    else:
        i = i + 1
        num = num

print num
