#Ex44

#prova1: implicito (la classe figlia eredita tutto -pass- dalla classe padre)
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


#prova2: override (la classe figlia sovrascrive la classe padre)
class Parent(object):

    def override(self):
        print "PARENT override()"


class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

#prova3: un caso speciale di overriding: correlato all'esecuzione o meno di classe padre.
class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()


#prova finale: combinazione
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

### COMPOSITION
print '*' * 30

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, before OTHER altered()"
        self.other.altered()
        print "CHILD, after OTHER altered()"


son = Child()

son.implicit()
son.override()
son.altered()

###finee###
