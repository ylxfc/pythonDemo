def cheese_and_crackers(cheess_count, boxes_of_crackers):
	print "you have %d cheess!" %cheess_count
	print "%d" %boxes_of_crackers
	print "get a blanket.\n"

print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
