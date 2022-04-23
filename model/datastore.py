from model.person import Person

class Store:
    def __init__(self):
        self.list=[]

    def add(self,newone):
        self.list.append(newone)

    def getpeople(self):
        return self.list

people=Store()
people.add(Person(1,'Raja','Chennai'))
people.add(Person(2,'Raju','Mumbai'))
people.add(Person(3,'Anna','Delhi'))
