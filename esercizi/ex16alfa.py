#study drills ex 16
"""Write a script similar to the last exercise that uses read and argv
to read the file you just created.
There's too much repetition in this file.
Use strings, formats, and escapes to print out line1,
line2, and line3 with just one target.write() command instead of six.
Find out why we had to pass a 'w' as an extra parameter to open.
Hint: open tries to be safe by making you explicitly say you want to write a file.
If you open the file with 'w' mode, then do you really need the target.truncate()?
Read the documentation for Python's open function and see if that's true."""

from sys import argv

script, filename = argv
print "We're going to open a file and read it."
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print target.read()
