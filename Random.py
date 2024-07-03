#from numpy import random
import numpy as np
from numpy.random import randint

output = np.random.randint(10)
print(output)



output = np.random.randint(2, 100)
print(output)


n = 100

# Step 1
alice_bits = randint(2, size=n)
alice_bases = randint(2, size=n)

print("alice_bits="+ str(alice_bits))
print("alice_bases="+str(alice_bases))