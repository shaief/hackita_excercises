#1st method:
for i in range(100): 
	print str(100-i) + "bottles of beer on the wall"

#2nd method:
print '\n'.join(['%d bottles of beer on the wall' % (100-i) for i in range(100)])

