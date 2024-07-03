x = range(6)

for n in x:
  print(n)




y = range(1,15)
for n in y:
    print(n)

print('===========================')

p = range(3, 22, 2)
for n in p:
   print(n)


a_list = [14,18,19,22,66]

import random
for j in range(5):
    print('* Results from sample', j + 1)
    print('\n    Random number from 0 to 1:', random.random())
    print("\n    Random choice from our list:", random.choice(a_list))
    print('\n')


print(range(6))