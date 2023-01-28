print(len("Programiz"))

print(len ([1,2,3,4]))

class Person:
    def __init__(self,title="default_title"):
        self._name=None
        self.title=title
    
    def talk(self):
        print("Im a person")
    
    def walk(self):
        print("Im a walking")

class Employee(Person):
    def __init__(self,id,title):
        super().__init__(title)
        self.id=id
    
    def talk(self):
        print("im an employee")

class SportPerson(Person):
    def __init__(self,id,title):
        super().__init__(title)
        self.id=id

    def talk(self):
        print("im sport")

person1=Person("p1")
person2=Employee(1,"p2")
person3=SportPerson(2,"p3")

def check_talk(obj):
    obj.talk()

print(person2.talk())