#Esercizio 15

from sys import argv

script, filename = argv #importa da prompt

# filename = raw_input("Type the name of the file oyu want to open:") #prova da input

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# study drills: chiudi i files

print txt.close()
print txt_again.close()


##fine
