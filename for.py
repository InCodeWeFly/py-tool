# for  test
items = ['cat', 'window', 'defenestrate', '13'];


if(0):
    for item in items:
        print(item, len(item),'\r\n')

    for i in range(len(items)):
        print(i, items[i])
        print(range(len(items)))

    for k in range(10):
        if k == 7:
            continue
        else:
            print(k)


repetitions = 1
for x in range(3):
    for y in range(repetitions):
        print("y="+str(y))
    repetitions *= 2
    print('repetitions='+ str(repetitions))




