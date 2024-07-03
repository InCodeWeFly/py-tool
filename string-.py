#
# https://www.w3schools.com/python/ref_string_format.asp
#

x = "Python is "
X = "PYTHON IS "
y = "awesome"
z =  x + y
print(z)

t = str(3)
print(t)

print(X)
print(x)

print(type(x))



txt = "I like bananas"
x   = txt.replace("bananas", "apples")
print(x)


txt = 'WJDJUEKDODLKOOD'
x   = txt.lower()
print(x)

txt = 'sdereeerer'
x   = txt.upper()
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
