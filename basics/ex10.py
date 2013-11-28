import sys
import operator

# open the text.txt file
f = open('book.txt', 'r')
#read the text.txt into a string
booktxt = f.read()

bookwords = booktxt.split()

words = {}

for word in bookwords:
	if word not in words:
		words[word] = 1
	else:
		words[word] +=1
word_max = max(words.iteritems(),key=operator.itemgetter(1))[0]

print "The word: '" + word_max + "' appeared: " +str(words[word_max]) + " times in the text"