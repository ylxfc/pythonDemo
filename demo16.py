from sys import argv 

script, filename = argv

print "we're going to erase %r." %filename
print "if you don't want that, hit CRTL-C(^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three linse."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
 
print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" %(line1, line2, line3))

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, We close it."
target.close()
