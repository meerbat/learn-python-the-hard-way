#Esercizio 42

class Animal(object):
    pass

##dog is a class of animal
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name


## person has an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has some kind of pet
        self.pet = None


## an employee is a class of person
class Employee(Person):
    def __init__(self, name, salary):

        #class X(object): def __init__(self, J)
        #"class X has-a __init__ that takes self and J parameters."
        ##magic??That's how you can run the __init__ method of a parent class reliably.
        #Search for "python super" and read the various advice on it being evil and good for you.
        super(Employee, self).__init__(name)
        ##employee has a salary
        self.salary = salary

## ?? da definire
class Fish(object):
    pass

## salmon is a kind of fish
class Salmon(Fish):
    pass

## halibut is a kind of fish
class Halibut(Fish):
    pass

## rover is a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

##mary's pet is satan
mary.pet = satan

## frank is an employee and has a 120000 salary
frank = Employee("Frank", 120000)

## rover is frank's pet
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
