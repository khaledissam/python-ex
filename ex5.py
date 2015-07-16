# -*- coding: utf-8 -*-

# ex5
name = 'mj'
age = 20
h = 74
w = 180

print 'The name is %s' % name
print "The age is %d" % age
print "Height = %d in, Weight = %d lb" %(h,w)

# ex6
x = "There are %d types of people." % 10
print x

y = "I said: %r." % x
print y

h = False
e = "Isn't that joke so funny?! %r"
print e % h

# ex7
x = "Mary had a little lamb"
y = x + ", little lamb" 
z = "." * 10
print x
print y
print z
print x,y,z

# ex8
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True,False,True,False)
print formatter % (formatter, formatter, formatter, formatter)

# ex9

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "days: ", days
print "months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# ex10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
