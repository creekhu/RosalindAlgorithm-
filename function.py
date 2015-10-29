def nigga(x):
    return 'hey ' + x

print nigga('kevin')

def hart(num):
    return num - 5

print hart(40)

#default parameter
def test(a = 'kevin', b = 'hart'):
    print '%s %s' % (a,b)

test()

test('tianqi','hu')
test('tianqi')
test(b='hu')
test(a='tianqi')
