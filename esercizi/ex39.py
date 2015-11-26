#Esercizio 39
interr = '-' * 10

#create a mapping of state and abbr.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#creates a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print interr
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print interr
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state's abbreviation
print interr
for state, abbrev in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)

#print every city in state
print interr
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now we do both at the same time
print interr
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print interr
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s." % city



###fine###
