#file for "Classes" section of Introduction to Python
class Greeter(object):
    def hello(self):
        print("Hello")

    def goodbye(self):
        print("Holla!!")

g = Greeter()
g.hello()
g.goodbye()