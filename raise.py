x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

try:
    f = open('file.txt', 'r')
except IOError:
    # do some processing here
    # and then pass the error on
    raise