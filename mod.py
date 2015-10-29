#import mod (not mod.py)
#mod.testmod()
#note that you can only import the modulus once
#if the modulus has been changed, you have to close the idle and import again
def testmod():
    print "hello nigga"

# or we can use reload method

# reload(mod)
# mod.testmod()

import math
print dir(math) # a list
print math.__doc__ # a shot prompt
print math.__name__
print math.__package__

help(math) # a long version 

