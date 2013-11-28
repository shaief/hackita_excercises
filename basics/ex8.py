import sys

def palindrom(user_word):
	for i in range(len(user_word)/2):
		if (user_word[i] <> user_word[-i-1]):
			#print user_word +" is not a palindrom!"
			return False
	#print user_word + " is a palindrom!!!"
	return True

# open the text.txt file
f = open('text.txt', 'r')
#read the text.txt into a string
texttxt = f.read()
print texttxt
palindromtxt = ""
words = texttxt.split()
for word in words:
	if palindrom(word): palindromtxt+=(" "+word)
print palindromtxt
