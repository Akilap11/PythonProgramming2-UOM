class Warrior:
    def __init__(self,name):
        self.name=name
        self.age=0

    @property #getter
    def age(self):
        return self.age
    
    @age.setter #setter
    def age(self,age):
        if(age>0):
            self.age=age
        else:
            print("Age should be greater than zero")

warrior=Warrior("WArrior 1")
warrior.age=-5
print(warrior.age)





class Person:
   def __init__(self,title="default_title"):
      self._name=None
      self.title=title
   def talk(self, words):
      print("talk 1")
   def talk(self, words):
      print("talk 2")


class Employee(Person):
   def __init__(self,id,title):
      super().__init__(xx)
      self.id=id

person1=Person()
person1.talk("Hello")

person2 = Person("Professor")
print (person2.title)