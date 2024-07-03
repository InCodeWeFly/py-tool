
try:
    print(True == False)
    print(True == 1)
    print(True == [])

    print('=====================')

    print(False == '')
    print(False == ' ')
    print(False == None)
    print(False == 0)

except Exception:
    print('Error!'+ Exception.message)