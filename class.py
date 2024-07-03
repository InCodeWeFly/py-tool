class Person:
    age = 7878

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def printName(self):
        print(self.username+ " "+self.password)


p1 = Person()
#print(p1.username)
#print(p1.password)
#print(p1.age)


#Inheritance 继承
class Student(Person):
    def __init__(self, username='', password=''):
        super().__init__(username,  password)


x = Student("Mike", "password")
x.printName()
print(x.__class__.__name__)
print(x.__class__.__base__)
print(x.__class__.__dict__)
print(x.__class__.__str__)


yes = hasattr(p1, 'age')
yes = hasattr(p1, 'printName')
yes = hasattr(p1, '__init__')
#yes = hasattr(p1, 'printName111')
#print('yes=', yes)