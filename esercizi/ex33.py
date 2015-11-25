#Esercizio 33

#i = 0

numbers = []

def sostituto(limite, incr):
    #sostiuiamo il while commentato.
    print "CIAO!" #stampa di prova se funge la funz.
    i = 0
    while i < limite:
        print "At the top i is %d." % i
        numbers.append(i)

        i += incr #affidiamo l'incremento ad una var per regolarlo meglio.
        print "Numbers now: ", numbers
        print "At the bottom i is %d." % i


"""
while i < 6:
    print "At the top i is %d." % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d." % i
"""
sost = sostituto(20, 6)

print sost

print "La tabellina:"

for num in numbers:
    print num


###fineee###
