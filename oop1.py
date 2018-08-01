class Agent1():
    def __init__(self, real_name):
        self.real_name = real_name
x = Agent1('James Bond')
print(x.real_name)

class Agent2():

    #Class object attribute
    planet = 'Earth'

    def __init__(self, real_name, eye_color, height):
        self.real_name = real_name
        self.eye_color = eye_color
        self.height = height
y = Agent2('James Bond', 'green',175)
print(y.real_name)
print(y.eye_color)
print(y.height)
print(y.planet)

z = Agent2('DBS','brown',165)
print(z.eye_color)
print(z.planet)

class Circle():
    pi = 3.141592

    #radius = 1 is the default value so I can make an object without entring a radius value
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi
    def perimeter(self):
        return 2 * self.radius * Circle.pi
    def report_something(self, name):
        print('Report {}'.format(name))
        return

mycircle = Circle(3)
print(mycircle.radius)
circle2 = Circle()
print(circle2.radius)
print(mycircle.area())
print(mycircle.perimeter())
mycircle.report_something('John')

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def report(self):
        print('I am {} {}'.format(self.first_name, self.last_name))
    def hello(self):
        print('hello!!')
p = Person('James','Bond')
p.report()

class Agent(Person):
    def __init__(self,first_name,last_name,code_name):
        Person.__init__(self,first_name,last_name)
        self.code_name = code_name
    
    #override the report method from Person
    def report(self):
        print('Sorry I can not tell you my real name')
        print('But you can call me {}'.format(self.code_name))
    
    def true_name(self,passcode):
        if passcode==123:
            print('Correct passcode')
            print('I am {} {}'.format(self.first_name, self.last_name))
        else:
            self.report()
    
    def _private_method(self):
        print('private method')

x = Agent(first_name='Alan',last_name='Turing',code_name='Hero')
x.hello()
x.report()
x.true_name(234)
x.true_name(123)

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #string representation of the object
    def __str__(self):
        return 'Title is {} and Author is {}'.format(self.title, self.author)

    def __len__(self):
        return self.pages

    def __del__(self):
        print ('A book has been deleted')

b = Book('Python Rocks', 'James Bond', 250)
print(b)
print(len(b))
del b
