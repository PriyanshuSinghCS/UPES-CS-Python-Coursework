class Person:
    def __init__(self, newAge, newName):
        self.age = newAge
        self.name = newName
    
    def displayAge(self):
        print("%s age %d" % (self.name, self.age))

def start():
    person1 = Person(13,"Person2")
    person2 = person1
    person1.displayAge()
    person2.displayAge()
    print()
    person1 = Person(888,"Person1")
    person1.displayAge()
    person2.displayAge()

p1 = Person(20, "Priyanshu")
p1.displayAge()
start()