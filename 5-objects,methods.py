#Class->Objects->Attributes->Methods

class Monster:
    color="black" #this is the only class attribute

    def __init__(self,age,name):
        self.age=age
        self.name=name
    
        self._is_innocent=None
    
    def steal(self,warrior):
        warrior.lose_stick()

m1=Monster(1,"aa")
print(m1.age)

m1.age=10
print(m1.age)

Monster.color="pink"
print(m1.color)
