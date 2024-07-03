def hello_world(data = None):
  print("Hello World")
  print(data)


hello_world()

# 变量只跟随名字
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His middle name is " + kid["mname"])


my_function(fname = "Tobias", lname = "Refsnes", mname = "lucas")




def testReturn() -> str:
    return True

print(testReturn())