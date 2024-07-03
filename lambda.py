

functionName = lambda a : a + 11
print(functionName(5))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))