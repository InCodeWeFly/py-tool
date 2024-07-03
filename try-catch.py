try:
    x = 1/0
    print(x)
except Exception:
    print(Exception.message)