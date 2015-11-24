# Esercizio 17
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#prova a farlo su una linea

#in_file = open(from_file)
#indata = in_file.read()
indata = open (from_file, 'r') #done!

print "The input file is %d bytes long" % len(from_file)

print "Does the output file exist? %r" % exists(to_file)
'''print "Ready, hit RETURN to continue, CTRL-c to abort."
raw_input()'''

out_file = open(to_file, 'w')
out_file.write(indata.read())
#attenta, se metti from_file copia in out_file il nome del file e non il suo contenuto!

print "Allright, all done."

out_file.close()


###fine###
