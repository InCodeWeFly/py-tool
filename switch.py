def test1():
    return "zero"


def test2():
    return "one"


def  test3():
    return "two"

#Python Object
switcher = {
    0: test1,
    1: test2,
    2: test3
}


def test(signal):
    # Get the function from switcher dictionary
    func = switcher.get(signal, "nothing")
    # Execute the function
    return func()


print(test(0))