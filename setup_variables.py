import random


def setup_variables():
    ### Replace this section with anything you want ###


    r = random.random()
    A = r * (2 / 3)
    B = r * (1 / 3)

    ### End of section ###
    return A, B



print(setup_variables())