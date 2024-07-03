from typing import TypeVar
from typing import NewType


S      = TypeVar("S")

UserId = NewType('UserId', int)
def getUserId(x: UserId):
    return x


print(getUserId(UserId(123456))) # this is fine
print(getUserId(123456))         # that's an int, not a UserId

print(UserId(123456) + 123456)   # fine, because UserId is a subclass of int


#print('111'+222)