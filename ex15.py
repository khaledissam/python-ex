from sys import argv

script, filename = argv

txt = open(filename)

print "File name = %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("OpenSees> ")

txt_again = open(file_again)

print txt_again.read()
