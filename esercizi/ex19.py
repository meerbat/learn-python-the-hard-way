#Esercizio 19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

#prova1
print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

#prova2
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prova3
print "We can even do Math inside it too:"
cheese_and_crackers(12 + 18, 4 + 7)

#prova4
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 900)

###fineee###
#studydrills#

def contafrutti(nome, mele, arance):
    print "\nTi chiami %s." % nome
    print "Hai %i mele." % mele
    print "Hai %i arance." % arance
    print "In totale hai %i frutti." % (mele+arance)

print "Prova direttamente (1):"
contafrutti("OLA", 7, 4)

print "Prova variabili (2):"
omino = "BU"
meline = 55
arancine = 33

contafrutti (omino, meline, arancine)

print "Prova matematica (3):"
contafrutti("CICCI"+"NO", 7+3, 9*2)

print "Prova combinata (4):"
contafrutti(omino+"LLO", meline+9, arancine+222)

#fine studydrills#
